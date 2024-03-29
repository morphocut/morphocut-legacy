import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from skimage.io import imread, ImageCollection
from skimage.color import rgb2gray
import numpy as np
from scipy.ndimage.filters import gaussian_filter1d
from skimage.exposure import rescale_intensity
from scipy.optimize import curve_fit
from vignetting2 import correct_vignetting
from skimage.filters import gaussian

# if "images" not in locals():
#     images = []

#     print("Reading collection...")
#     for img in ImageCollection("/data1/mschroeder/Datasets/18-10-15_Sediment_Trap_Fred_LeMoigne/*/*.jpeg"):
#         images.append(img)

#     min_height = min(img.shape[0] for img in images)
#     min_width = min(img.shape[1] for img in images)

#     images = [img[:min_height, :min_width] for img in images]

# print("Mean...")
# img = np.mean(images, axis=0)
img = imread(
    "/home/moi/Work/18-10-15 Sediment Trap Fred LeMoigne/M138 T4 600B cleaned/T4 600B 4.jpeg")

img = rgb2gray(img)

# Blur image
img = gaussian(img, 3)

print(img.shape)

# print("Correcting...")
# img_corrected = np.mean([correct_vignetting(img) for img in images], axis=0)


def imshow_with_marginals(img, marg_agg=np.mean):
    fig = plt.figure()

    gs = GridSpec(2, 3, width_ratios=[1, 3, 0.1], height_ratios=[3, 1])
    ax_joint = plt.subplot(gs[0, 1])
    ax_marg_x = plt.subplot(gs[1, 1], sharex=ax_joint)
    ax_marg_y = plt.subplot(gs[0, 0], sharey=ax_joint)

    # Turn off tick labels on marginals
    # plt.setp(ax_marg_x.get_xticklabels(), visible=False)
    # plt.setp(ax_marg_y.get_yticklabels(), visible=False)

    SIGMA = 100
    MODE = "reflect"
    ax_img = ax_joint.imshow(img, extent=(0, img.shape[1], 0, img.shape[0]),
                             aspect="auto")
    marg_x = marg_agg(img, axis=0)
    marg_x_smooth = gaussian_filter1d(marg_x, SIGMA, mode=MODE)
    center_x = np.argmax(marg_x_smooth)
    marg_y = marg_agg(img, axis=1)
    marg_y_smooth = gaussian_filter1d(marg_y, SIGMA, mode=MODE)
    center_y = np.argmax(marg_y_smooth)

    ax_marg_x.plot(marg_x)
    ax_marg_x.plot(marg_x_smooth)
    ax_marg_x.axvline(center_x)
    # ax_marg_x.set_ylim(0, 1)

    ax_marg_y.plot(marg_y, np.arange(img.shape[0]))
    ax_marg_y.plot(marg_y_smooth, np.arange(img.shape[0]))
    ax_marg_y.axhline(center_y)
    # ax_marg_y.set_xlim(0, 1)

    ax_joint.plot(center_x, center_y, marker='o', markersize=3, color="red")

    ax_color = plt.subplot(gs[0, 2])
    fig.colorbar(ax_img, cax=ax_color)

    #fig.savefig("results/vignetting.pdf", bbox_inches="tight")


imshow_with_marginals(rescale_intensity(img), marg_agg=np.min)

#_, _, img = correct_vignetting(img)

# imshow_with_marginals(rescale_intensity(rgb2gray(img_corrected)))
