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


def get_properties_list(properties, object_id):
    '''
    Iterates through the regionprops and adds them to a list of dictionaries. 
    
    Returns: the list of dictionaries
    '''
    prop_list = []
    for property in properties:
        propDict = {'img_file_name':  object_id+'_'+str(property.label)+'.png',
                        'object_id':  object_id+'_'+str(property.label),

                        'centroid_row':  property.centroid[0],
                        'centroid_col':  property.centroid[1],

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
    return prop_list


def export_image_regions(properties, object_id, original, mask):
    '''
    Iterates through the region properties and exports images containing each object
    '''
    print('exporting object images!')
    i = 0
    bar = ProgressBar(len(properties), max_width=40)
    for property in properties:
        # print('exporting object: '+str(i))
        x = property.bbox[0]
        y = property.bbox[1]
        w = property.bbox[2]-property.bbox[0]
        h = property.bbox[3]-property.bbox[1]

        bordersize_w = int(w / 2)
        bordersize_h = int(h / 2)

        xmin = max(0, x-bordersize_w)
        xmax = min(original.shape[0], x+w+bordersize_w)
        ymin = max(0, y-bordersize_h)
        ymax = min(original.shape[1], y+h+bordersize_h)

        original_masked = original[xmin:xmax, ymin:ymax]
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

        filename = object_id+'_'+str(property.label)+'.png'
        filepath = os.path.join('segmentation_export', filename)
        cv.imwrite(filepath, object_image)
        i += 1
        bar.numerator += 1
        print(bar, end="\r")

    print()


def import_image():
    # ----------------START IMPORTING------------------------

    if len(sys.argv) < 2:
        print('Argument missing. Please provide a valid path to an image file.')
        exit(0)

    source_filename = sys.argv[1]

    object_id = parse("{}.{}", source_filename)[0]
    # object_id = 'T4 200a-04'

    src = cv.imread(source_filename)
    original = src

    if src is None:
        print('Could not open or find the image:', args.input)
        exit(0)

    return src, original, object_id


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


def process_image(src, original):
    # ----------------START IMAGE PROCESSING------------------------

    # Show source image

    imageSize = 0.4

    src = cv.resize(src, None, fx=imageSize, fy=imageSize)

    # cv.imshow('Source Image', original)

    src = flatten_colors(src)

    src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # src = cv.GaussianBlur(src,(11,11),0)

    src = cv.resize(src, None, fx=1/imageSize, fy=1/imageSize)

    # src = cv.equalizeHist(src)

    cv.imwrite('grey_blur_image.png', src)

    # _ ,mask = cv.threshold(src, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # mask = cv.bitwise_not(mask)

    _ ,mask = cv.threshold(src, 90, 255, cv.THRESH_BINARY)
    mask = cv.bitwise_not(mask)

    # mask = cv.adaptiveThreshold(src,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,55,3)
    # kernel = np.ones((5,5), np.uint8) 
    # mask = cv.dilate(mask, kernel, iterations=1) 

    # cv.imshow('Threshold Image', mask)

    _, markers = cv.connectedComponents(mask)

    # cv.imshow('Marker Image', markers)

    properties = measure.regionprops(markers, coordinates='rc')
    # properties = [p for p in properties if p.area > 10]
    # print(str(centroids))
    print(str(len(properties))+' objects found!')

    masked = cv.bitwise_and(original,original,mask = mask)

    # cv.imshow('Masked Image', masked)

    return src, mask, properties
    # ----------------END IMAGE PROCESSING------------------------


def export(original, mask, properties, object_id):
    # ----------------START EXPORTING------------------------

    print('exporting object properties!')
    prop_list = get_properties_list(properties, object_id)
    prop_frame = pd.DataFrame(prop_list)
    filepath = os.path.join('segmentation_export', 'export.csv')
    prop_frame.to_csv(filepath, sep='\t', encoding='utf-8', index=False)

    mask_color = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    masked_overlay = cv.addWeighted(original, 0.7, mask_color, 0.3, 0)
    cv.imwrite('masked.png', masked_overlay)


    export_image_regions(properties, object_id, original, mask)


    # ----------------END EXPORTING------------------------




if __name__ == "__main__":
    src, original, object_id = import_image()
    src, mask, properties = process_image(src, original)
    export(original, mask, properties, object_id)



