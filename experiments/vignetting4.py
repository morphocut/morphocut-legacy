"""
As the vignetting effect is highly assymmetrical and
therefore seems not to be create by one single aperture,
try Splines.
"""

import operator

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from skimage.color import rgb2gray
from skimage.filters import gaussian, scharr, threshold_otsu
from skimage.filters.rank import maximum
from skimage.io import imread
from skimage.morphology import binary_dilation, binary_erosion, dilation, disk

from vignetting2 import tiled_threshold
import scipy.ndimage as ndi
from skimage.morphology import reconstruction

print("Loading...")
img = imread(
    "/home/moi/Work/18-10-15 Sediment Trap Fred LeMoigne/M138 T4 600B cleaned/T4 600B 4.jpeg")

img = rgb2gray(img)

sigma0 = 3
sigma1 = 10

# Blur image to make dilation more robust
img0 = gaussian(img, sigma0)
img1 = gaussian(img, sigma1)

dog = img1 - img0

# Find edges by thresholding on dog
thr = threshold_otsu(dog)

seed = np.zeros_like(img0) + img0.max()

edges = binary_dilation(dog > thr, disk(2))

edge_labels, num_labels = ndi.label(edges)
for lbl, slc in enumerate(ndi.find_objects(edge_labels, num_labels)):
    mask = edge_labels[slc] > 0
    seed[slc][mask] = img0[slc][mask]

rec = reconstruction(seed, img0, method="erosion")

objs = rec <= img0

# invalid = seed > mask
# seed[invalid] = mask[invalid]

# # Find obvious objects
# thr = threshold_otsu(img)
# # thr = np.quantile(img, 0.0625)
# valid_mask = img > thr
# #valid_mask = tiled_threshold(img, n=5, op=operator.gt)

# # Shrink valid regions
# valid_mask = binary_erosion(valid_mask, disk(16))

# print("Dilating...")
# max_img = dilation(img, disk(16))

# # img_inpaint = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

# invalid_mask = np.bitwise_not(valid_mask)

# valid_mask &= binary_dilation(invalid_mask, disk(1))

# # Interpolate masked image
# print("Fitting interpolator...")
# coords = np.array(np.nonzero(valid_mask)).T
# values = max_img[valid_mask]

# interpolator = interpolate.LinearNDInterpolator(coords, values)

# print("Interpolating {:,d}px...".format(invalid_mask.sum()))
# img_filled = max_img.copy()
# coords_invalid = np.array(np.nonzero(invalid_mask)).T
# img_filled[invalid_mask] = interpolator(coords_invalid)

# mask = np.isnan(img_filled)
# img_filled[mask] = max_img[mask]

# # Blur background
# print("Blurring...")
# img_filled = gaussian(img_filled, 64)

fig, axes = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True)

axes[0, 0].imshow(img, cmap="gray")
axes[0, 1].imshow(dog)
axes[0, 2].imshow(dog > thr)
axes[1, 0].imshow(seed, cmap="gray")
axes[1, 1].imshow(rec, cmap="gray")
axes[1, 2].imshow(objs)
