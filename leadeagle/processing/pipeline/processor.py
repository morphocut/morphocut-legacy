import math

from skimage import img_as_ubyte, measure
from skimage.exposure import rescale_intensity
from skimage.morphology import binary_dilation, disk

import cv2 as cv
import leadeagle.processing.functional as F
from leadeagle.processing.pipeline import NodeBase


class Processor(NodeBase):
    """
    A processing node. Performs segmentation on images to find objects and their region properties
    """

    def __call__(self, input=None):
        for data_object in input:
            print('Processing file ' +
                  data_object['facets']['input_data']['meta']['filepath'])
            yield from self.process_single_image(data_object)

    def process_single_image(self, data_object):
        src = data_object['facets']['corrected_data']['image']

        # Segment foreground objects from background objects using thresholding with the otsu method
        _, mask = cv.threshold(src, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        mask = cv.bitwise_not(mask)

        # Find connected components in the masked image to identify individual objects
        _, markers = cv.connectedComponents(mask)

        # Retrieve regionprops of the connected components and filter out those who are smaller than 30 pixels in area
        areaThreshold = 30
        properties = measure.regionprops(markers, coordinates='rc')
        properties = [p for p in properties if p.area > areaThreshold]

        yield from self.export_image_regions(data_object, properties)

    def export_image_regions(self, data_object, properties):
        '''
        Iterates through the region properties and exports images containing each object
        '''

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

            new_object = dict(
                object_id='{}_{}'.format(data_object['object_id'], i),
                raw_img=dict(
                    id=i,
                    meta=dict(properties=property),
                    image=original_masked
                ),
                contour_img=dict(
                    image=contours_masked
                ),
            )

            yield new_object


class VignetteCorrector(NodeBase):
    """
    A processing node. Removes the vignette effect from images.
    """

    def __call__(self, input=None):
        for data_object in input:
            data_object['facets']['corrected_data'] = dict(
                image=self.correct_vignette(
                    data_object['facets']['input_data']['image'])
            )
            yield data_object

    def correct_vignette(self, img):
        grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        flat_image = F.calculate_flat_image(grey_img)
        corrected_img = grey_img / flat_image
        corrected_img = rescale_intensity(corrected_img)

        return corrected_img
