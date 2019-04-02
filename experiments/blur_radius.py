"""
Tang, C., Hou, C. and Song, Z. (2013) ‘Defocus map estimation from a single image via spectrum contrast.’,
Optics letters, 38(10), pp. 1706–8. doi: 10.1364/OL.38.001706.
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
from skimage.feature import canny
from skimage.filters import gaussian, scharr, threshold_otsu
from skimage.io import imread
from skimage.morphology import dilation
from skimage.measure import label
from skimage.color import label2rgb

img = imread(
    "/data1/mschroeder/Datasets/19-02-21-FredLeMoigne/M138 T4 (wetransfer-477f42)/M138 T4 300A-02.jpeg")

# img = imread("/data1/mschroeder/Downloads/Blume-5.jpg")

#img = img[:, :1000]

img = rgb2gray(img)

# Find step edges(canny edge detector)
edges = canny(img, sigma=1, use_quantiles=True,
              low_threshold=0.80, high_threshold=0.90)

edges = canny(img)

# Reblur edge using a known Gaussian kernel
# sigma0 is the standard deviation of the re-blur Gaussian kernel
sigma0 = 10
img_reblurred = gaussian(img, sigma=sigma0)

# Calculate gradient magnitudes before and after blurring (Eq. 8)
img_grad = scharr(img)
reblurred_grad = scharr(img_reblurred)

diff = img_grad - reblurred_grad

thresh = threshold_otsu(diff)


# Calculate gradient magnitude ratio at edge locations (Eq. 6)
#R = img_grad / reblurred_grad

R = img_grad / reblurred_grad

# Maximum filter to suppress pepper noise
#R = dilation(R, disk(4))

# Calculate unknown blur amount sigma (Eq. 7)
sigma = sigma0 / np.sqrt(R**2 - 1)

# Apply joint bilateral filtering to refine those inaccurate blur estimates (Eq. 9)
# skimage.util.view_as_windows

# Defocus map interpolation (Levin 2008)

# # Linear interpolation
# valid_mask = edges & np.isfinite(sigma)
# coords = np.array(np.nonzero(valid_mask)).T
# interpolator = LinearNDInterpolator(coords, sigma[valid_mask])
# sigma_dense = sigma.copy()
# coords_invalid = np.array(np.nonzero(~valid_mask)).T
# sigma_dense[~valid_mask] = interpolator(coords_invalid)

cmap = plt.cm.get_cmap()
cmap.set_bad(color='black')

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
axes[0, 0].imshow(img, cmap="gray", label="img")
fig.colorbar(axes[0, 1].imshow(diff, label="diff"), ax=axes[0, 1])
fig.colorbar(axes[1, 0].imshow(
    label2rgb(label(diff > thresh)), label="R"), ax=axes[1, 0])
# fig.colorbar(axes[2, 0].imshow(
#     np.ma.array(sigma, mask=~edges), norm=LogNorm(), label="sigma"),
#     ax=axes[2, 0])
# fig.colorbar(axes[2, 1].imshow(sigma_dense, norm=LogNorm(), label="sigma_dense"),
#              ax=axes[2, 1])
