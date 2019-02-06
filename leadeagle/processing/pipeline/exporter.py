from leadeagle.processing.pipeline import NodeBase
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


class Exporter(NodeBase):
    """
    An importing node. Imports images based on the filepath
    """

    def __init__(self, location):
        self.location = location
        self.init_date = datetime.datetime.now().strftime('%Y_%m_%d')

    def __call__(self, input=None):
        # hier zip öffnen!!
        for data_object in input:
            print('Exporting file '
                  + data_object['facets']['input_data']['meta']['filepath'])
            self.export_data(data_object)
            # yield wp

    def get_property_column_types(self):
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

    def get_properties_list(self, original):
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

    def export_data(self, data_object):

        # Define the filename and full path for the zip file
        zip_filename = 'ecotaxa_segmentation_{}.zip'.format(self.init_date)
        zip_filepath = os.path.join(self.location, zip_filename)

        # If the path does not exist, create it
        if not os.path.exists(self.location):
            os.makedirs(self.location)

        # Create the zip file
        with ZipFile(zip_filepath, 'a', zipfile.ZIP_DEFLATED) as myzip:

            # prop_list = []
            # prop_list.insert(0, get_property_column_types())
            for new_object in data_object['facets']['processed_data']:
                # Collect the information on the object into a list of dictionaries
                # prop_list_single = get_properties_list(original)
                # prop_list.extend(prop_list_single)
                # Calculate the masked images for the object and write them to the zip file
                # export_image_regions(original, myzip)

                filename = "{}_{}.png".format(
                    data_object['object_id'], new_object['raw_img']['id'])
                img_str = cv.imencode('.png', new_object['raw_img']['image'])[
                    1].tostring()
                myzip.writestr(filename, img_str)

                filename = "{}_{}_contours.png".format(
                    data_object['object_id'], new_object['raw_img']['id'])
                img_str = cv.imencode('.png', new_object['contour_img']['image'])[
                    1].tostring()
                myzip.writestr(filename, img_str)

            # Transform the list into a dataframe
            # prop_frame = pd.DataFrame(prop_list)

            # Write the dataframe as a tsv file to the zip file
            # sio = StringIO()
            # filepath = 'ecotaxa_segmentation.tsv'
            # prop_frame.to_csv(sio, sep='\t', encoding='utf-8', index=False)
            # myzip.writestr(filepath, sio.getvalue())

        return zip_filename
