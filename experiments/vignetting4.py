"""
As the vignetting effect is highly assymmetrical and
therefore seems not to be create by one single aperture,
try Splines.
"""

import operator

import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi
from scipy import interpolate

from skimage import img_as_ubyte
from skimage.color import rgb2gray
from skimage.filters import gaussian, scharr, threshold_otsu
from skimage.filters.rank import maximum
from skimage.io import imread
from skimage.morphology import (binary_dilation, binary_erosion, dilation,
                                disk, reconstruction)
from skimage.segmentation import flood
from tqdm import tqdm

print("Loading...")
# img = imread(
#     "/home/moi/Work/18-10-15 Sediment Trap Fred LeMoigne/M138 T4 600B cleaned/T4 600B 4.jpeg")
img = imread(
    "/data1/mschroeder/Datasets/19-02-21-FredLeMoigne/M138 T4 (wetransfer-477f42)/M138 T4 300A-13.jpeg")

img = rgb2gray(img)

sigma0 = 4
sigma1 = 12

# Blur image to make dilation more robust
img0 = gaussian(img, sigma0)
img1 = gaussian(img, sigma1)

dog = img1 - img0

# Find edges by thresholding on dog
thr = threshold_otsu(dog)

edges = binary_dilation(dog > thr, disk(3))

#rec = dilation(img0, disk(3))
rec = img0.copy()

print("Erasing objects...")
edge_labels, num_labels = ndi.label(edges)
for lbl in tqdm(range(num_labels)):
    edge_mask = edge_labels == lbl + 1
    edge_max = rec[edge_mask].max()
    edge_min = rec[edge_mask].min()

    lower = (rec <= edge_min) | edge_mask

    seed_point = tuple(np.transpose(np.nonzero(edge_mask))[0])
    flooded = flood(img_as_ubyte(lower), seed_point)
    rec[flooded] = edge_max

objs = rec > img0
objs = binary_dilation(objs, disk(3))

fig, axes = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True)

axes[0, 0].imshow(img, cmap="gray")
axes[0, 1].imshow(dog)
axes[0, 2].imshow(dog > thr)
rec_ax = axes[1, 0].imshow(rec, cmap="gray")
obj_ax = axes[1, 1].imshow(objs, cmap="gray")
# axes[1, 2].imshow(, cmap="gray")
