import matplotlib.pyplot as plt
import itertools
from skimage.filters import threshold_otsu, gaussian
from skimage.color import rgb2gray
import numpy as np
from skimage.io import ImageCollection
import getpass


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


def remove_objects(image, n=5):
    """
    Parameters:
        image (np.ndarray of shape = [h,w,c]): Image to clear.
        n: number of slices per spatial dimension.
    """

    image = image.copy()
    image_gray = rgb2gray(image)

    for s in create_slices(image_gray.shape, n):
        tile = image[s]
        tile_gray = image_gray[s]

        try:
            thr = threshold_otsu(tile_gray)
        except ValueError:
            pass
        else:
            obj_mask = tile_gray < thr

            bg_mean = np.mean(tile[~obj_mask], axis=(0, 1))

            tile[obj_mask] = bg_mean

    return image


user = getpass.getuser()

if (user == 'Christian'):
    img_collection = ImageCollection(
        "C:\Bibliotheken\Dokumente\hiwi_geomar\LeadEagle\Test\Images for Rainer\*\*.jpeg")
else:
    img_collection = ImageCollection(
        "/data1/mschroeder/Datasets/18-10-15_Sediment_Trap_Fred_LeMoigne/*/*.jpeg")

img = img_collection[1]

img2 = remove_objects(img, 5)

# Maybe use spline interpolation instead? May be faster?
# https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
img3 = gaussian(img2, 75, multichannel=True)

corrected = img / img3 / 255

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
axes[0, 0].imshow(img)
axes[0, 1].imshow(img2)
axes[1, 0].imshow(img3)
axes[1, 1].imshow(corrected)

plt.show()
