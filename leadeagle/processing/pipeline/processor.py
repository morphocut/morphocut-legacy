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


class Processor(NodeBase):
    """
    An importing node. Imports images based on the filepath
    """

    # {
    #     object_id: ...
    #     facets: {
    #         # For DataLoader
    #         input_data: {
    #             meta: {filename: ...},
    #             image: <np.array of shape = [h,w,c]>
    #         },
    #         # For Processor
    #         raw_img: {
    #             meta: {region props...},
    #             image: <np.array of shape = [h,w,c]>
    #         },
    #         contour_img: {
    #             meta: {},
    #             image: <np.array of shape = [h,w,c]>
    #         },
    #         # Nothing for export
    #     }
    # }

    def __call__(self, input=None):
        # data_object = input.__next__()
        for data_object in input:
            print('Processing file ' +
                  data_object['facets']['input_data']['meta']['filepath'])
            yield from self.process_single_image(data_object)
            # yield data_object
            # data_object = input.__next__()

    def export_image_regions(self, data_object, properties):
        '''
        Iterates through the region properties and exports images containing each object
        '''

        objects = []
        # bar = ProgressBar(len(properties)), max_width=40)
        for i, property in enumerate(properties):

            src_img = data_object['facets']['input_data']['image']

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
            xmax = min(src_img.shape[0], x + w + bordersize_w)
            ymin = max(0, y - bordersize_h)
            ymax = min(src_img.shape[1], y + h + bordersize_h)

            border_top = y - ymin
            border_bottom = ymax - (y + h)
            border_left = x - xmin
            border_right = xmax - (x + w)

            # Create the masked and the masked contour image of the object
            original_masked = src_img[xmin:xmax, ymin:ymax]

            bordered_mask = cv.copyMakeBorder(img_as_ubyte(property.filled_image), top=border_left,
                                              bottom=border_right, left=border_top, right=border_bottom, borderType=cv.BORDER_CONSTANT)

            f = 0.1
            dilated_mask = img_as_ubyte(binary_dilation(
                bordered_mask, selem=disk(radius=f * math.sqrt(property.filled_area))))

            c_img, contours, hierarchy = cv.findContours(dilated_mask, 1, 2)
            contour_image = original_masked.copy()
            cv.drawContours(contour_image, contours, -1, (0, 255, 0), 1)

            contours_masked = contour_image


            # vars(property) => robustes property.__dict__
            new_object = dict(
                raw_img=dict(
                    id=i,
                    meta=dict(
                        properties=property,
                    ),
                    image=original_masked
                ),
                contour_img=dict(
                    image=contours_masked
                ),
            )

            yield new_object

        #     bar.numerator = i + 1
        #     print(bar, end="\r")

        # print()
        # data_object['facets']['processed_data'] = objects

    def process_single_image(self, data_object):
        src = self.correct_vignette(
            data_object['facets']['input_data']['image'])

        # Segment foreground objects from background objects using thresholding with the otsu method
        _, mask = cv.threshold(src, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        mask = cv.bitwise_not(mask)

        # Find connected components in the masked image to identify individual objects
        _, markers = cv.connectedComponents(mask)

        # Retrieve regionprops of the connected components and filter out those who are smaller than 30 pixels in area
        areaThreshold = 30
        properties = measure.regionprops(markers, coordinates='rc')
        properties = [p for p in properties if p.area > areaThreshold]

        # Save the calculated properties and images to a dictionary
        # data_object['facets']['raw_img']['meta']['regionprops'] = properties

        yield from self.export_image_regions(data_object, properties)

    def correct_vignette(self, img):

        grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        flat_image = proc.calculate_flat_image(grey_img)
        corrected_img = grey_img / flat_image
        corrected_img = rescale_intensity(corrected_img)
        corrected_img = img_as_ubyte(corrected_img)

        return corrected_img
