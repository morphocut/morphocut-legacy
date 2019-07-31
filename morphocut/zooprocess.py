from morphocut.graph import Node, Output, Input
import os
from PIL import Image
import numpy as np
from skimage import filters
from skimage.morphology import disk
from pprint import pprint


@Output("image")
@Output("filename")
class ZooProcessLoader(Node):
    """Loads a directory containing ZooScan TIFs."""

    def __init__(self, root):
        super().__init__()
        self.root = root

    def transform_stream(self, stream):
        for root, _, filenames in os.walk(self.root):
            for fn in filenames:
                _, ext = os.path.splitext(fn)

                if ext.lower() == ".tif":
                    image = np.asarray(Image.open(os.path.join(root, fn)))

                    yield self.prepare_output({}, (image, fn))


@Input("image")
@Output("flat")
class RollingBall(Node):
    """Calculates a flat-field image by using the "rolling ball" algorithm."""

    def __init__(self, radius):
        super().__init__()
        self.selem = disk(radius)

    def transform(self, image):
        return filters.rank.maximum(image, self.selem)


@Input("image")
@Output("mask")
class ThresholdOtsu(Node):
    """Calculate a mask using Otsu's method."""

    def __init__(self, radius):
        super().__init__(self)
        self.selem = disk(radius)

    def transform(self, image):
        return filters.rank.maximum(image, self.selem)


def zooprocess():
    """
    MorphoCut implementation of the ZooProcess pipeline.

    This pipeline is meant to be compatible with the latest version of ZooProcess.
    """
    # Data loading
    loader = ZooProcessLoader("/home/moi/Work/fake-zooscan")

    # "Rolling Ball"
    rollingball = RollingBall(16)(loader.image)

    # Thresholding

    # Extraction of masks
