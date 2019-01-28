import matplotlib.pyplot as plt
import itertools
from skimage.filters import threshold_otsu, gaussian
from skimage.color import rgb2gray
import numpy as np
from skimage.io import ImageCollection
import operator


def create_slices(shape, n):
    """
    Create tiles
    Parameters:
        shape (tuple):
        n: number of slices per spatial dimension.
    """

    slices = []
    for dim in shape:
        tile_size = dim // n
        slices.append(
            [slice(i * tile_size, (i + 1) * tile_size if i < (n - 1) else None)
             for i in range(n)]
        )

    return list(itertools.product(*slices))


def remove_objects(image, n=5, agg=np.mean):
    """
    Parameters:
        image (np.ndarray of shape = [h,w]): Image to clear.
        n: number of slices per spatial dimension.
    """

    image = image.copy()

    for s in create_slices(image.shape, n):
        tile = image[s]

        try:
            thr = threshold_otsu(tile)
        except ValueError:
            pass
        else:
            obj_mask = tile < thr

            bg_mean = agg(tile[~obj_mask])

            tile[obj_mask] = bg_mean

    return image


def tiled_threshold(img, n=5, op=operator.lt):
    mask = np.zeros(img.shape[:2], dtype=np.bool)

    for s in create_slices(img.shape, n):
        tile = img[s]
        try:
            thr = threshold_otsu(tile)
        except ValueError:
            pass

        mask[s] = op(tile, thr)

    return mask


def correct_vignetting(img):
    img_gray = rgb2gray(img)
    img_gray = remove_objects(img_gray, 5, agg=np.median)

    img_smooth = gaussian(img_gray, 75)

    return img_gray, img_smooth, img / img_smooth[:, :, np.newaxis] / 255


if __name__ == "__main__":
    img_collection = ImageCollection(
        "/data1/mschroeder/Datasets/18-10-15_Sediment_Trap_Fred_LeMoigne/*/*.jpeg")

    img = img_collection[1]

    img_gray, img_smooth, corrected = correct_vignetting(img)

    fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
    axes[0, 0].imshow(img)
    axes[0, 1].imshow(img_gray, cmap="gray")
    axes[1, 0].imshow(img_smooth, cmap="gray")
    axes[1, 1].imshow(corrected)
