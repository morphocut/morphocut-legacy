"""
As the vignetting effect is highly assymmetrical and
therefore seems not to be create by one single aperture,
try Splines.
"""

from skimage.io import imread
from skimage.color import rgb2gray
from skimage.feature import canny
import matplotlib.pyplot as plt
from skimage.filters.rank import maximum
from skimage.morphology import disk
from skimage import img_as_uint
from skimage.morphology import dilation, binary_erosion
import numpy as np
from skimage.filters import gaussian
from scipy.ndimage.morphology import distance_transform_cdt
from skimage.filters import threshold_otsu
from scipy import interpolate

print("Loading...")
img = imread(
    "/home/moi/Work/18-10-15 Sediment Trap Fred LeMoigne/M138 T4 600B cleaned/T4 600B 4.jpeg")

img = rgb2gray(img)

# Blur image to make dilation more robust

img = gaussian(img, 3)

# Find obvious objects
thr = threshold_otsu(img)

valid_mask = img > thr

valid_mask = binary_erosion(valid_mask, disk(16))

print("Dilating...")
max_img = dilation(img, disk(16))

# img_inpaint = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

invalid_mask = ~valid_mask

valid_mask &= dilation(invalid_mask, disk(1))

# Interpolate masked image
print("Fitting interpolator...")
coords = np.array(np.nonzero(valid_mask)).T
values = max_img[valid_mask]

interpolator = interpolate.LinearNDInterpolator(coords, values)

print("Interpolating {:,d}px...".format(invalid_mask.sum()))
img_filled = max_img.copy()
coords_invalid = np.array(np.nonzero(invalid_mask)).T
img_filled[invalid_mask] = interpolator(coords_invalid)

mask = np.isnan(img_filled)
img_filled[mask] = max_img[mask]

fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)

vmax = max_img.max()
axes[0, 0].imshow(img, vmin=0, vmax=vmax)
axes[0, 1].imshow(img_filled, vmin=0, vmax=vmax)
axes[1, 0].imshow(invalid_mask, cmap="gray")
axes[1, 1].imshow(img / img_filled)
