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


def get_properties_list(original):
    '''
    Iterates through the regionprops and adds them to a list of dictionaries.

    Returns: the list of dictionaries
    '''
    prop_list = []
    i = 1
    for property in original['properties']:
        propDict = {'img_file_name':  original['object_id']+'_'+str(i)+'.png',
                        'object_id':  original['object_id']+'_'+str(i),

                        'centroid_row':  property.centroid[0],
                        'centroid_col':  property.centroid[1],

                        'position_row':  property.coords[0],
                        'position_col':  property.coords[1],

                        'diameter_equivalent':  property.equivalent_diameter,
                        'length_minor_axis':  property.minor_axis_length,
                        'length_major_axis':  property.major_axis_length,
                        # 'ratio_eccentricity' :  property.eccentricity,
                        'perimeter':  property.perimeter,
                        'orientation':  property.orientation,

                        'area':  property.area,
                        'area_convex':  property.convex_area,
                        'area_filled':  property.filled_area,
                        'box_min_row':  property.bbox[0],
                        'box_max_row':  property.bbox[2],
                        'box_min_col':  property.bbox[1],
                        'box_max_col':  property.bbox[3],
                        'ratio_extent':  property.extent,
                        'ratio_solidity':  property.solidity,

                        'countCoords':  len(property.coords)}
        prop_list.append(propDict)
        i += 1
    return prop_list


def export_image_regions(original):
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
        object_image = original_masked
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
        filepath = os.path.join('segmentation_export', filename)
        cv.imwrite(filepath, object_image)
        i += 1
        bar.numerator += 1
        print(bar, end="\r")

    print()


def import_data():
    # ----------------START IMPORTING------------------------

    if len(sys.argv) < 2:
        print('Argument missing. Please provide a valid path to an image file.')
        exit(0)
        
    originals = []

    source_filePath = sys.argv[1]
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

    # object_id = parse("{}.{}", fileName)[0]

    # src = cv.imread(source_filepath)
    # original = src

    # cv.imshow("", original)
    # cv.waitKey()

    # if src is None:
    #     print('Could not open or find the image:', args.input)
    #     exit(0)

    return originals


    # ----------------END IMPORTING------------------------


def flatten_colors(src, K=4):
    '''
    Flattens the colors of the image, such that the image consists of only K colors
    '''
    img = src.copy()
    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    # cv.imshow('flattened image ', res2)
    # cv.waitKey()

    return res2


def process_single_image(original):
    # ----------------START IMAGE PROCESSING------------------------

    src = original['img']

    src = flatten_colors(src)

    src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # _ ,mask = cv.threshold(src, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # mask = cv.bitwise_not(mask)

    _ ,mask = cv.threshold(src, 90, 255, cv.THRESH_BINARY)
    mask = cv.bitwise_not(mask)

    # mask = cv.adaptiveThreshold(src,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,55,3)
    # kernel = np.ones((5,5), np.uint8) 
    # mask = cv.dilate(mask, kernel, iterations=1) 

    _, markers = cv.connectedComponents(mask)

    # retrieve regionprops of the connected components and filter those who are smaller than 15 pixels in area
    areaThreshold = 15
    properties = measure.regionprops(markers, coordinates='rc')
    properties = [p for p in properties if p.area > areaThreshold]

    print(original['object_id']+': '+str(len(properties))+' objects found!')

    masked = cv.bitwise_and(original['img'],original['img'],mask = mask)

    original['mask'] = mask
    original['properties'] = properties

    # return src, mask, properties
    # ----------------END IMAGE PROCESSING------------------------


def export_data(originals):
    # ----------------START EXPORTING------------------------

    # print('exporting object properties!')

    dirName = 'segmentation_export'
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    # with ZipFile('segmentation_export_'+datetime.datetime.now+'.zip', 'w') as myzip:
        # myzip.write('eggs.txt')

    prop_list = []
    for original in originals:
        prop_list_single = get_properties_list(original)
        prop_list.extend(prop_list_single)
        export_image_regions(original)

    prop_frame = pd.DataFrame(prop_list)
    filepath = os.path.join('segmentation_export', 'segmentation_export.tsv')
    prop_frame.to_csv(filepath, sep='\t', encoding='utf-8', index=False)

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
    filepath = os.path.join('segmentation_export', 'general_properties_export.tsv')
    prop_frame.to_csv(filepath, sep='\t', encoding='utf-8', index=False)

    # mask_color = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    # masked_overlay = cv.addWeighted(original, 0.7, mask_color, 0.3, 0)
    # cv.imwrite('masked.png', masked_overlay)


    # ----------------END EXPORTING------------------------




if __name__ == "__main__":
    originals = import_data()
    for original in originals:
        process_single_image(original)
    export_data(originals)


    # src, mask, properties = process_single_image(src, original)
    # export_data(original, mask, properties, object_id)



