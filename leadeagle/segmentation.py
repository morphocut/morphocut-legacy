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


def get_property_column_types():
    propDict = {'img_file_name':  '[t]',

                    'object_id':  '[t]',
                    'object_date':  '[t]',
                    'object_time':  '[t]',
                    'object_width':  '[f]',
                    'object_height':  '[f]',
                    'object_area':  '[f]',
                    'object_major_axis_length':  '[f]',
                    'object_minor_axis_length':  '[f]',
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
                    # 'object_max_intensity': '[f]',
                    # 'object_mean_intensity': '[f]',
                    # 'object_min_intensity': '[f]',
                    'object_perimeter': '[f]',
                    'object_solidity': '[f]',
                    # 'object_weighted_centroid_row': '[f]',
                    # 'object_weighted_centroid_col': '[f]',
                    # 'object_weighted_local_centroid_row': '[f]',
                    # 'object_weighted_local_centroid_col': '[f]',
                }
    return propDict


def get_properties_list(original):
    '''
    Iterates through the regionprops and adds them to a list of dictionaries.

    Returns: the list of dictionaries
    '''
    prop_list = []
    i = 1

    for property in original['properties']:
        propDict = {'img_file_name':  str(original['object_id']+'_'+str(i)+'.png'),

                    'object_id':  str(original['object_id']+'_'+str(i)),
                    'object_date':  str(datetime.datetime.now().strftime('%Y%m%d')),
                    'object_time':  str(datetime.datetime.now().strftime('%H%M%S')),
                    'object_width':  property.bbox[3] - property.bbox[1],
                    'object_height':  property.bbox[2] - property.bbox[0],
                    'object_area':  property.area,
                    'object_major_axis_length':  property.major_axis_length,
                    'object_minor_axis_length':  property.minor_axis_length,
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
                    # 'object_max_intensity': property.max_intensity, 
                    # 'object_mean_intensity': property.mean_intensity, 
                    # 'object_min_intensity': property.min_intensity, 
                    'object_perimeter': property.perimeter, 
                    'object_solidity': property.solidity, 
                    # 'object_weighted_centroid_row': property.weighted_centroid[0], 
                    # 'object_weighted_centroid_col': property.weighted_centroid[1], 
                    # 'object_weighted_local_centroid_row': property.weighted_local_centroid[0], 
                    # 'object_weighted_local_centroid_col': property.weighted_local_centroid[1], 
                    }
        prop_list.append(propDict)
        i += 1
    return prop_list


def export_image_regions(original, zip):
    '''
    Iterates through the region properties and exports images containing each object
    '''
    print(original['object_id']+': exporting object images!')
    i = 0
    bar = ProgressBar(len(original['properties']), max_width=40)
    for property in original['properties']:
        # print('exporting object: '+str(i))
        x = property.bbox[0]
        y = property.bbox[1]
        w = property.bbox[2]-property.bbox[0]
        h = property.bbox[3]-property.bbox[1]

        bordersize_w = int(w / 2)
        bordersize_h = int(h / 2)

        xmin = max(0, x-bordersize_w)
        xmax = min(original['img'].shape[0], x+w+bordersize_w)
        ymin = max(0, y-bordersize_h)
        ymax = min(original['img'].shape[1], y+h+bordersize_h)

        original_masked = original['img'][xmin:xmax, ymin:ymax]
        contours_masked = original['contour_img'][xmin:xmax, ymin:ymax]

        # object_image = original_masked
        # mask_masked = mask[x:x+w, y:y+h]

        # object_image = cv.bitwise_and(
        #     original_masked, original_masked, mask=mask_masked)
        # coloured = object_image.copy()
        # object_image[mask_masked == 0] = (255, 255, 255)
        # object_image = cv.cvtColor(object_image, cv.COLOR_BGR2GRAY)

        # bordersize = 20
        # object_image = cv.copyMakeBorder(object_image, top=bordersize, bottom=bordersize, left=bordersize,
        #                     right=bordersize, borderType=cv.BORDER_CONSTANT, value=[255, 255, 255])

        filename = original['object_id']+'_'+str(i)+'.png'
        img_str = cv.imencode('.png', original_masked)[1].tostring()
        zip.writestr(filename, img_str)

        filename = original['object_id']+'_'+str(i)+'_contours.png'
        img_str = cv.imencode('.png', contours_masked)[1].tostring()
        zip.writestr(filename, img_str)

        i += 1
        bar.numerator += 1
        print(bar, end="\r")

    print()


def import_data(source_filePath):

    originals = []
    
    folderName, fileName = os.path.split(source_filePath)

    if (fileName.endswith('.jpeg')):
        print('importing '+source_filePath)
        object_id = parse("{}.{}", fileName)[0]
        img = cv.imread(source_filePath)
        originals.append(dict(object_id=object_id, img=img))
    else:
        for root, dirs, files in os.walk(source_filePath, topdown=False):
            for name in files:
                if (name.endswith('.jpeg')):
                    print('importing '+os.path.join(root, name))
                    filePath = os.path.join(root, name)
                    object_id = parse("{}.{}", name)[0]
                    img = cv.imread(filePath)
                    originals.append(dict(object_id=object_id, img=img))

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

    src = flatten_colors(src)

    src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # _ ,mask = cv.threshold(src, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # mask = cv.bitwise_not(mask)

    _, mask = cv.threshold(src, 90, 255, cv.THRESH_BINARY)
    mask = cv.bitwise_not(mask)

    # mask = cv.adaptiveThreshold(src,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,55,3)
    # kernel = np.ones((5,5), np.uint8)
    # mask = cv.dilate(mask, kernel, iterations=1)

    _, markers = cv.connectedComponents(mask)

    # retrieve regionprops of the connected components and filter those who are smaller than 15 pixels in area
    areaThreshold = 15
    properties = measure.regionprops(markers, coordinates='rc')
    properties = [p for p in properties if p.area > areaThreshold]

    c_img, contours, hierarchy = cv.findContours(mask, 1, 2)
    contour_image = original['img'].copy()
    cv.drawContours(contour_image, contours, -1, (0, 255, 0), 1)

    # cv.imshow('contour image', contour_image)
    # cv.waitKey()

    print(original['object_id']+': '+str(len(properties))+' objects found!')

    masked = cv.bitwise_and(original['img'], original['img'], mask=mask)

    original['mask'] = mask
    original['properties'] = properties
    original['contour_img'] = contour_image


def export_data(originals, export_path):

    # dirName = 'segmentation_export'
    # if not os.path.exists(dirName):
    #     os.makedirs(dirName)

    zip_relativepath = 'ecotaxa_segmentation_' + \
        str(datetime.datetime.now().strftime('%Y_%m_%d'))+'.zip'
    zip_filepath = os.path.join(export_path, 'ecotaxa_segmentation_' + \
        str(datetime.datetime.now().strftime('%Y_%m_%d'))+'.zip')

    with ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as myzip:

        prop_list = []
        prop_list.insert(0, get_property_column_types())
        for original in originals:
            prop_list_single = get_properties_list(original)
            prop_list.extend(prop_list_single)
            export_image_regions(original, myzip)
        prop_frame = pd.DataFrame(prop_list)

        sio = StringIO()
        filepath = 'ecotaxa_segmentation.tsv'
        prop_frame.to_csv(sio, sep='\t', encoding='utf-8', index=False)
        myzip.writestr(filepath, sio.getvalue())

        general_properties = []
        for original in originals:
            total_area = original['img'].shape[0] * original['img'].shape[1]
            total_area_filled = 0
            for p in original['properties']:
                total_area_filled += p.area
            propDict = {'object_id':  original['object_id'],
                        'total_area': total_area,
                        'total_area_filled': total_area_filled,
                        'area_filled': (total_area_filled / total_area)}
            general_properties.append(propDict)
        prop_frame = pd.DataFrame(general_properties)

        sio = StringIO()
        filepath = 'ecotaxa_general.tsv'
        prop_frame.to_csv(sio, sep='\t', encoding='utf-8', index=False)
        myzip.writestr(filepath, sio.getvalue())

    return zip_relativepath


def process(source_filepath, export_path):
    originals = import_data(source_filepath)
    print('importing files from '+source_filepath)
    for original in originals:
        process_single_image(original)
    zip_filepath = export_data(originals, export_path)
    return zip_filepath


if __name__ == "__main__":
    print('main')
    if len(sys.argv) < 2:
        print('Argument missing. Please provide a valid path to an image file.')
        exit(0)
    source_filePath = sys.argv[1]

    process(source_filePath, '')
