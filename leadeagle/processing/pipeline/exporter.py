from leadeagle.processing.pipeline import NodeBase
import cv2 as cv
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
import random
import string


class Exporter(NodeBase):
    """
    Ecotaxa Export

    Writes a .zip-Archive with the following entries:
        - ecotaxa_segmentation.csv
        - <objid>.png
        - <objid>_contours.png

    TODO: Make exported images configurable

    Input:

    {
        object_id: ...
        raw_img: {
            id: ...
            meta: {region props...},
            image: <np.array of shape = [h,w,c]>
        },
        contour_img: {
            image: <np.array of shape = [h,w,c]>
        }
    }

    """

    def __init__(self, archive_fn):
        self.archive_fn = archive_fn

    def __call__(self, input=None):
        print('exporter call')
        with ZipFile(self.archive_fn, 'w', zipfile.ZIP_DEFLATED) as myzip:

            prop_list = []
            prop_list.append(self.get_property_column_types())

            for data_object in input:

                filename = "{}.png".format(
                    data_object['object_id'])
                img_str = cv.imencode('.png', data_object['raw_img']['image'])[
                    1].tostring()
                myzip.writestr(filename, img_str)
                prop_list.append(
                    self.get_properties_list(data_object, filename, img_rank=1))

                filename = "{}_{}.png".format(
                    data_object['object_id'], 'contours')
                img_str = cv.imencode('.png', data_object['contour_img']['image'])[
                    1].tostring()
                myzip.writestr(filename, img_str)
                prop_list.append(
                    self.get_properties_list(data_object, filename, img_rank=2))

            # Transform the list into a dataframe
            prop_frame = pd.DataFrame(prop_list)

            # Write the dataframe as a tsv file to the zip file
            sio = StringIO()
            filepath = 'ecotaxa_segmentation.tsv'
            prop_frame.to_csv(sio, sep='\t', encoding='utf-8', index=False)
            myzip.writestr(filepath, sio.getvalue())

        # Exporter has no output
        yield None

    def get_property_column_types(self):
        '''
        Returns the column types for the columns in the tsv file for the ecotaxa export
        '''
        propDict = {'img_file_name': '[t]',
                    'img_rank': '[f]',
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

    def get_properties_list(self, data_object, filename, img_rank):
        '''
        Transforms the region properties of the data object into the tsv export format.
        '''
        property = data_object['raw_img']['meta']['properties']
        propDict = {
            'img_file_name': filename,  # img_file_name
            'img_rank': img_rank,  # img_rank
            'object_id': data_object['object_id'],  # object_id
            # object_date
            'object_date': str(datetime.datetime.now().strftime('%Y%m%d')),
            # object_time
            'object_time': str(datetime.datetime.now().strftime('%H%M%S')),
            # object_width
            'object_width': property.bbox[3] - property.bbox[1],
            # object_height
            'object_height': property.bbox[2] - property.bbox[0],
            'object_bx': property.bbox[1],
            'object_by': property.bbox[0],
            'object_circ.': (4 * math.pi * property.area) / math.pow(property.perimeter, 2),
            'object_area': property.area,  # object_area
            'object_major_axis_length': property.major_axis_length,  # object_major_axis_length
            'object_minor_axis_length': property.minor_axis_length,  # object_minor_axis_length
            'object_bounding_box_area': property.bbox_area,  # object_bounding_box_area
            'object_y': property.centroid[0],  # object_centroid_row
            'object_x': property.centroid[1],  # object_centroid_col
            'object_convex_area': property.convex_area,  # object_convex_area
            'object_eccentricity': property.eccentricity,  # object_eccentricity
            # object_equivalent_diameter
            'object_equivalent_diameter': property.equivalent_diameter,
            'object_euler_number': property.euler_number,  # object_euler_number
            'object_extent': property.extent,  # object_extent
            'object_filled_area': property.filled_area,  # object_filled_area
            # object_local_centroid_row
            'object_local_centroid_row': property.local_centroid[0],
            # object_local_centroid_col
            'object_local_centroid_col': property.local_centroid[1],
            'object_perim.': property.perimeter,  # object_perimeter
            'object_solidity': property.solidity,  # object_solidity
        }

        return propDict
