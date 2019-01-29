import cv2 as cv
import numpy as np
import argparse
from skimage import measure
import pandas as pd
import os
from parse import *
import sys
from etaprogress.progress import ProgressBar
import matplotlib.pyplot as plt
import datetime
from io import StringIO
from zipfile import ZipFile
import zipfile
import leadeagle.processing.functional as proc
from skimage.exposure import rescale_intensity
from skimage.morphology import binary_dilation, disk
from skimage import img_as_ubyte
import math


def get_property_column_types():
    '''
    Returns the column types for the columns in the tsv file for the ecotaxa export
    '''
    propDict = {'img_file_name': '[t]',
                'contour_img_file_name': '[t]',
                'object_id': '[t]',
                'object_date': '[t]',
                'object_time': '[t]',
                'object_width': '[f]',
                'object_height': '[f]',
                'object_area': '[f]',
                'object_major_axis_length': '[f]',
                'object_minor_axis_length': '[f]',
                'object_bounding_box_area': '[f]',
                'object_centroid_row': '[f]',
                'object_centroid_col': '[f]',
                'object_convex_area': '[f]',
                'object_eccentricity': '[f]',
                'object_equivalent_diameter': '[f]',
                'object_euler_number': '[f]',
                'object_extent': '[f]',
                'object_filled_area': '[f]',
                'object_local_centroid_row': '[f]',
                'object_local_centroid_col': '[f]',
                'object_perimeter': '[f]',
                'object_solidity': '[f]',
                }
    return propDict


def get_properties_list(original):
    '''
    Iterates through the regionprops and adds them to a list of dictionaries.

    Returns: the list of dictionaries
    '''
    prop_list = []

    for i, property in enumerate(original['properties']):
        propDict = {
            'img_file_name': "{}_{}.png".format(original['object_id'], i),
            'contour_img_file_name': "{}_{}_contours.png".format(original['object_id'], i),
            'object_id': "{}_{}".format(original['object_id'], i),
            'object_date': str(datetime.datetime.now().strftime('%Y%m%d')),
            'object_time': str(datetime.datetime.now().strftime('%H%M%S')),
            'object_width': property.bbox[3] - property.bbox[1],
            'object_height': property.bbox[2] - property.bbox[0],
            'object_area': property.area,
            'object_major_axis_length': property.major_axis_length,
            'object_minor_axis_length': property.minor_axis_length,
            'object_bounding_box_area': property.bbox_area,
            'object_centroid_row': property.centroid[0],
            'object_centroid_col': property.centroid[1],
            'object_convex_area': property.convex_area,
            'object_eccentricity': property.eccentricity,
            'object_equivalent_diameter': property.equivalent_diameter,
            'object_euler_number': property.euler_number,
            'object_extent': property.extent,
            'object_filled_area': property.filled_area,
            'object_local_centroid_row': property.local_centroid[0],
            'object_local_centroid_col': property.local_centroid[1],
            'object_perimeter': property.perimeter,
            'object_solidity': property.solidity,
        }
        prop_list.append(propDict)
    return prop_list


def export_image_regions(original, zip):
    '''
    Iterates through the region properties and exports images containing each object
    '''
    print(original['object_id'] + ': exporting object images!')

    bar = ProgressBar(len(original['properties']), max_width=40)
    for i, property in enumerate(original['properties']):

        # Define bounding box and position of the object
        x = property.bbox[0]
        y = property.bbox[1]
        w = property.bbox[2] - property.bbox[0]
        h = property.bbox[3] - property.bbox[1]

        # Define bordersize based on the width and height of the object. The border size specifies how much of the image around the object is shown in its image.
        bordersize_w = int(w / 2)
        bordersize_h = int(h / 2)

        # Calculate min and max values for the border around the object, so that there are no array errors (no value below 0, no value above max width/height).
        xmin = max(0, x - bordersize_w)
        xmax = min(original['img'].shape[0], x + w + bordersize_w)
        ymin = max(0, y - bordersize_h)
        ymax = min(original['img'].shape[1], y + h + bordersize_h)

        border_top = y - ymin
        border_bottom = ymax - (y + h)
        border_left = x - xmin
        border_right = xmax - (x + w)

        # print('src (w/h): ' + str(w) + ', ' + str(h))
        # print('border_top: ' + str(border_top))
        # print('border_bottom: ' + str(border_bottom))
        # print('border_left: ' + str(border_left))
        # print('border_right: ' + str(border_right))

        # Create the masked and the masked contour image of the object
        original_masked = original['src'][xmin:xmax, ymin:ymax]

        bordered_mask = cv.copyMakeBorder(img_as_ubyte(property.filled_image), top=border_left,
                                          bottom=border_right, left=border_top, right=border_bottom, borderType=cv.BORDER_CONSTANT)

        f = 0.1
        dilated_mask = img_as_ubyte(binary_dilation(
            bordered_mask, selem=disk(radius=f * math.sqrt(property.filled_area))))

        c_img, contours, hierarchy = cv.findContours(dilated_mask, 1, 2)
        contour_image = original_masked.copy()
        cv.drawContours(contour_image, contours, -1, (0, 255, 0), 1)

        contours_masked = contour_image
        # contours_masked = original['contour_img'][xmin:xmax, ymin:ymax]

        # print('original: ' + str(original_masked.shape))
        # print('bordered: ' + str(bordered_mask.shape))
        # print('contour: ' + str(contour_image.shape))

        # cv.imshow('contours', contour_image)
        # cv.waitKey()

        # Save the created images to the zipfile
        filename = "{}_{}.png".format(original['object_id'], i)
        img_str = cv.imencode('.png', original_masked)[1].tostring()
        zip.writestr(filename, img_str)

        filename = "{}_{}_contours.png".format(original['object_id'], i)
        img_str = cv.imencode('.png', contours_masked)[1].tostring()
        zip.writestr(filename, img_str)

        bar.numerator = i + 1
        print(bar, end="\r")

    print()


def import_data(source_filePath):
    '''
    Imports the data from the path specified in source_filePath
    '''

    originals = []

    # If source_filePath points to a file, separate its filename from the path
    folderName, fileName = os.path.split(source_filePath)

    # If it is an image file, load it
    if (fileName.endswith('.jpeg')):
        print('importing ' + source_filePath)
        object_id = parse("{}.{}", fileName)[0]
        img = cv.imread(source_filePath)
        corrected_img = correct_vignette(img)
        originals.append(dict(object_id=object_id, img=corrected_img, src=img))
    # If it is not an image file, load the image files in the folder
    else:
        for root, dirs, files in os.walk(source_filePath, topdown=False):
            for name in files:
                if (name.endswith('.jpeg')):
                    print('importing ' + os.path.join(root, name))
                    filePath = os.path.join(root, name)
                    object_id = parse("{}.{}", name)[0]
                    img = cv.imread(filePath)
                    corrected_img = correct_vignette(img)
                    originals.append(
                        dict(object_id=object_id, img=corrected_img, src=img))

    return originals


def flatten_colors(src, K=4):
    '''
    Flattens the colors of the image, such that the image consists of only K colors
    '''
    img = src.copy()
    Z = img.reshape((-1, 3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv.kmeans(
        Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    return res2


def process_single_image(original):

    src = original['img']

    # Convert the image into grayscale colorspace
    # cv.imshow(str(src.dtype), src)
    # cv.waitKey()
    # src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # Segment foreground objects from background objects using thresholding with the otsu method
    _, mask = cv.threshold(src, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    mask = cv.bitwise_not(mask)

    # Alternative to otsu method, using adaptive thresholding
    # mask = cv.adaptiveThreshold(src,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,55,3)
    # kernel = np.ones((5,5), np.uint8)
    # mask = cv.dilate(mask, kernel, iterations=1)

    # Find connected components in the masked image to identify individual objects
    _, markers = cv.connectedComponents(mask)

    # Retrieve regionprops of the connected components and filter out those who are smaller than 30 pixels in area
    areaThreshold = 30
    properties = measure.regionprops(markers, coordinates='rc')
    properties = [p for p in properties if p.area > areaThreshold]

    # Create an image with the contours of all the objects marked
    # c_img, contours, hierarchy = cv.findContours(mask, 1, 2)
    # contour_image = original['src'].copy()
    # cv.drawContours(contour_image, contours, -1, (0, 255, 0), 1)

    print(original['object_id'] + ': ' +
          str(len(properties)) + ' objects found!')

    # masked = cv.bitwise_and(original['img'], original['img'], mask=mask)

    # Save the calculated properties and images to a dictionary
    original['mask'] = mask
    original['properties'] = properties
    # original['contour_img'] = contour_image


def correct_vignette(img):
    # size_0 = img.shape[0]
    # size_1 = img.shape[1]
    # border_0 = int(size_0 / 10)
    # border_1 = int(size_1 / 10)
    # vignette_cut_img = img[border_0:size_0 -
    #                        border_0, border_1:size_1 - border_1]

    # cv.imshow('original', img)
    # cv.imshow('removed vignette', vignette_cut_img)
    # cv.waitKey()

    grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    flat_image = proc.calculate_flat_image(grey_img)
    corrected_img = grey_img / flat_image
    corrected_img = rescale_intensity(corrected_img)
    corrected_img = img_as_ubyte(corrected_img)

    # cv.imshow(str(corrected_img.dtype), corrected_img)
    # cv.waitKey()

    return corrected_img


def export_data(originals, export_path):

    # print('export_path: '+export_path)

    # Define the filename and full path for the zip file
    zip_filename = 'ecotaxa_segmentation_' + \
        str(datetime.datetime.now().strftime('%Y_%m_%d')) + '.zip'
    zip_filepath = os.path.join(export_path, zip_filename)

    # If the path does not exist, create it
    if not os.path.exists(export_path):
        os.makedirs(export_path)

    # Create the zip file
    with ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as myzip:

        prop_list = []
        prop_list.insert(0, get_property_column_types())
        for original in originals:
            # Collect the information on the object into a list of dictionaries
            prop_list_single = get_properties_list(original)
            prop_list.extend(prop_list_single)
            # Calculate the masked images for the object and write them to the zip file
            export_image_regions(original, myzip)

        # Transform the list into a dataframe
        prop_frame = pd.DataFrame(prop_list)

        # Write the dataframe as a tsv file to the zip file
        sio = StringIO()
        filepath = 'ecotaxa_segmentation.tsv'
        prop_frame.to_csv(sio, sep='\t', encoding='utf-8', index=False)
        myzip.writestr(filepath, sio.getvalue())

        # Create a second tsv file containing general information about the processed images
        # general_properties = []
        # for original in originals:
        #     total_area = original['img'].shape[0] * original['img'].shape[1]
        #     total_area_filled = 0
        #     for p in original['properties']:
        #         total_area_filled += p.area
        #     propDict = {'object_id': original['object_id'],
        #                 'total_area': total_area,
        #                 'total_area_filled': total_area_filled,
        #                 'area_filled': (total_area_filled / total_area)}
        #     general_properties.append(propDict)
        # prop_frame = pd.DataFrame(general_properties)

        # sio = StringIO()
        # filepath = 'ecotaxa_general.tsv'
        # prop_frame.to_csv(sio, sep='\t', encoding='utf-8', index=False)
        # myzip.writestr(filepath, sio.getvalue())

    return zip_filename


def process(source_filepath, export_path):
    '''
    Imports images from the path specified in source_filepath and then performs segmentation on the images.
    The new image data and statistics are exported to a zip-file at the path specified in export_path.
    '''
    # Import the data from source_filepath
    originals = import_data(source_filepath)
    print('importing files from ' + source_filepath + ' done!')

    # Process the data
    for original in originals:
        process_single_image(original)

    # Export the data
    zip_filepath = export_data(originals, export_path)

    print('processing done!')

    return zip_filepath


if __name__ == "__main__":
    print('main')
    if len(sys.argv) < 2:
        print('Argument missing. Please provide a valid path to an image file.')
        exit(0)
    source_filePath = sys.argv[1]

    process(source_filePath, '')
