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


def get_properties_list(original):
    '''
    Iterates through the regionprops and adds them to a list of dictionaries.

    Returns: the list of dictionaries
    '''
    prop_list = []
    i = 1

    propDict = {'img_file_name':  '[t]',
                'img_rank':  '[f]',

                'object_id':  '[t]',
                'object_link':  '[t]',
                'object_lat':  '[f]',
                'object_long':  '[f]',
                'object_date':  '[t]',
                'object_time':  '[t]',
                'object_depth_min':  '[f]',
                'object_depth_max':  '[f]',
                'object_bx':  '[f]',
                'object_by':  '[f]',
                'object_width':  '[f]',
                'object_height':  '[f]',
                'object_area':  '[f]',
                'object_mean':  '[f]',
                'object_major':  '[f]',
                'object_minor':  '[f]',
                'object_feret':  '[f]',
                'object_area_exc':  '[f]',
                'object_thickr':  '[f]',
                'object_esd':  '[f]',
                'object_elongation':  '[f]',
                'object_range':  '[f]',
                'object_meanpos':  '[f]',
                'object_centroids':  '[f]',
                'object_cv':  '[f]',
                'object_sr':  '[f]',
                'object_perimareaexc':  '[f]',
                'object_perimferet':  '[f]',
                'object_perimmajor':  '[f]',
                'object_circex':  '[f]',
                'object_cdexc':  '[f]',
                'object_annotation_date':  '[t]',
                'object_annotation_time':  '[t]',
                'object_annotation_category':  '[t]',
                'object_annotation_person_name':  '[t]',
                'object_annotation_person_email':  '[t]',
                'object_annotation_status':  '[t]',

                'process_id':  '[t]',
                'process_date':  '[t]',
                'process_time':  '[t]',
                'process_software':  '[t]',
                'process_first_img':  '[f]',
                'process_last_img':  '[f]',
                'process_pressure_gain':  '[f]',
                'process_calibration':  '[t]',
                'process_pixel':  '[f]',
                'process_upper':  '[f]',
                'process_gamma':  '[f]',
                'process_esdmin':  '[f]',
                'process_esdmax':  '[f]',

                'acq_id':  '[t]',
                'acq_sn':  '[t]',
                'acq_volimage':  '[f]',
                'acq_aa':  '[f]',
                'acq_exp':  '[f]',
                'acq_pixel':  '[f]',
                'acq_file_description':  '[t]',
                'acq_tasktype':  '[f]',
                'acq_disktype':  '[f]',
                'acq_shutterspeed':  '[f]',
                'acq_gain':  '[f]',
                'acq_threshold':  '[f]',
                'acq_smbase':  '[f]',
                'acq_smzoo':  '[f]',
                'acq_erase_border_blob':  '[f]',
                'acq_choice':  '[f]',
                'acq_ratio':  '[f]',

                'sample_id':  '[t]',
                'sample_profileid':  '[t]',
                'sample_cruise':  '[t]',
                'sample_ship':  '[t]',
                'sample_stationid':  '[t]',
                'sample_bottomdepth':  '[t]',
                'sample_ctdrosettefilename':  '[t]',
                'sample_dn':  '[t]',
                'sample_winddir':  '[f]',
                'sample_windspeed':  '[f]',
                'sample_seastate':  '[f]',
                'sample_nebulousness':  '[f]',
                'sample_yoyo':  '[t]',
                'sample_comment':  '[t]',
                'sample_dataportal_descripteur':  '[t]',
                'sample_barcode':  '[t]',
                }
    prop_list.append(propDict)

    for property in original['properties']:
        propDict = {'img_file_name':  str(original['object_id']+'_'+str(i)+'.png'),
                    'img_rank':  'nan',

                    'object_id':  str(original['object_id']+'_'+str(i)),
                    'object_link':  'nan',
                    'object_lat':  'nan',
                    'object_long':  'nan',
                    'object_date':  str(datetime.datetime.now().strftime('%Y%m%d')),
                    'object_time':  str(datetime.datetime.now().strftime('%H%M%S')),
                    'object_depth_min':  'nan',
                    'object_depth_max':  'nan',
                    'object_bx':  'nan',
                    'object_by':  'nan',
                    'object_width':  property.bbox[3] - property.bbox[1],
                    'object_height':  property.bbox[2] - property.bbox[0],
                    'object_area':  property.area,
                    'object_mean':  'nan',
                    'object_major':  property.major_axis_length,
                    'object_minor':  property.minor_axis_length,
                    'object_feret':  'nan',
                    'object_area_exc':  'nan',
                    'object_thickr':  'nan',
                    'object_esd':  'nan',
                    'object_elongation':  'nan',
                    'object_range':  'nan',
                    'object_meanpos':  'nan',
                    'object_centroids':  property.centroid,
                    'object_cv':  'nan',
                    'object_sr':  'nan',
                    'object_perimareaexc':  'nan',
                    'object_perimferet':  'nan',
                    'object_perimmajor':  'nan',
                    'object_circex':  'nan',
                    'object_cdexc':  'nan',
                    'object_annotation_date':  'nan',
                    'object_annotation_time':  'nan',
                    'object_annotation_category':  'nan',
                    'object_annotation_person_name':  'nan',
                    'object_annotation_person_email':  'nan',
                    'object_annotation_status':  'nan',

                    'process_id':  'nan',
                    'process_date':  'nan',
                    'process_time':  'nan',
                    'process_software':  'nan',
                    'process_first_img':  'nan',
                    'process_last_img':  'nan',
                    'process_pressure_gain':  'nan',
                    'process_calibration':  'nan',
                    'process_pixel':  'nan',
                    'process_upper':  'nan',
                    'process_gamma':  'nan',
                    'process_esdmin':  'nan',
                    'process_esdmax':  'nan',

                    'acq_id':  'nan',
                    'acq_sn':  'nan',
                    'acq_volimage':  'nan',
                    'acq_aa':  'nan',
                    'acq_exp':  'nan',
                    'acq_pixel':  'nan',
                    'acq_file_description':  'nan',
                    'acq_tasktype':  'nan',
                    'acq_disktype':  'nan',
                    'acq_shutterspeed':  'nan',
                    'acq_gain':  'nan',
                    'acq_threshold':  'nan',
                    'acq_smbase':  'nan',
                    'acq_smzoo':  'nan',
                    'acq_erase_border_blob':  'nan',
                    'acq_choice':  'nan',
                    'acq_ratio':  'nan',

                    'sample_id':  'nan',
                    'sample_profileid':  'nan',
                    'sample_cruise':  'nan',
                    'sample_ship':  'nan',
                    'sample_stationid':  'nan',
                    'sample_bottomdepth':  'nan',
                    'sample_ctdrosettefilename':  'nan',
                    'sample_dn':  'nan',
                    'sample_winddir':  'nan',
                    'sample_windspeed':  'nan',
                    'sample_seastate':  'nan',
                    'sample_nebulousness':  'nan',
                    'sample_yoyo':  'nan',
                    'sample_comment':  'nan',
                    'sample_dataportal_descripteur':  'nan',
                    'sample_barcode':  'nan',




                    # 'centroid_row':  property.centroid[0],
                    # 'centroid_col':  property.centroid[1],

                    # 'position_row':  property.coords[0],
                    # 'position_col':  property.coords[1],

                    # 'diameter_equivalent':  property.equivalent_diameter,
                    # 'length_minor_axis':  property.minor_axis_length,
                    # 'length_major_axis':  property.major_axis_length,
                    # # 'ratio_eccentricity' :  property.eccentricity,
                    # 'perimeter':  property.perimeter,
                    # 'orientation':  property.orientation,

                    # 'area':  property.area,
                    # 'area_convex':  property.convex_area,
                    # 'area_filled':  property.filled_area,
                    # 'box_min_row':  property.bbox[0],
                    # 'box_max_row':  property.bbox[2],
                    # 'box_min_col':  property.bbox[1],
                    # 'box_max_col':  property.bbox[3],
                    # 'ratio_extent':  property.extent,
                    # 'ratio_solidity':  property.solidity,

                    # 'countCoords':  len(property.coords)
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
        # filepath = os.path.join('segmentation_export', filename)
        filepath = filename

        # cv.imwrite(filepath, object_image)
        img_str = cv.imencode('.png', object_image)[1].tostring()
        zip.writestr(filepath, img_str)

        i += 1
        bar.numerator += 1
        print(bar, end="\r")

    print()


def import_data():

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

    print(original['object_id']+': '+str(len(properties))+' objects found!')

    masked = cv.bitwise_and(original['img'], original['img'], mask=mask)

    original['mask'] = mask
    original['properties'] = properties


def export_data(originals):

    dirName = 'segmentation_export'
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    zip_filepath = 'segmentation_export_' + \
        str(datetime.datetime.now().strftime('%Y_%m_%d'))+'.zip'

    with ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as myzip:

        prop_list = []
        for original in originals:
            prop_list_single = get_properties_list(original)
            prop_list.extend(prop_list_single)
            export_image_regions(original, myzip)
        prop_frame = pd.DataFrame(prop_list)

        sio = StringIO()
        filepath = 'segmentation_export.tsv'
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
        filepath = 'general_properties_export.tsv'
        prop_frame.to_csv(sio, sep='\t', encoding='utf-8', index=False)
        myzip.writestr(filepath, sio.getvalue())


if __name__ == "__main__":

    originals = import_data()
    for original in originals:
        process_single_image(original)
    export_data(originals)
