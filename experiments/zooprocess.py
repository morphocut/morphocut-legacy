import os

import matplotlib.pyplot as plt
from skimage.color import gray2rgb
from timer_cm import Timer

import cv2
from morphocut.processing.pipeline import *
from morphocut.processing.pipeline.color import GrayToRGB
from morphocut.processing.pipeline.zooprocess_reader import ZooProcessReader
from PIL import Image
from skimage.io import imsave

Image.MAX_IMAGE_PIXELS = None

print("Preparing...")
reader = ZooProcessReader(
    # Data file
    "/data1/mschroeder/Thesis/thesis-data/M106_lrg_Sorted_vignettes/m106_mn01_n1_lrg_20150702_1150_pred_validated_ER_20150703/Pred_20150702_m106_mn01_n1_lrg_dat1.txt",
    # Raw images
    [
        "/data1/mschroeder/Thesis/thesis-data/M106_raw_lrg/M106_mn01_n1_lrg_1/M106_mn01_n1_lrg_1_1a.png",
        "/data1/mschroeder/Thesis/thesis-data/M106_raw_lrg/M106_mn01_n1_lrg_1/M106_mn01_n1_lrg_1_1b.png"
    ],
    sorted_dir="/data1/mschroeder/Thesis/thesis-data/M106_lrg_Sorted_vignettes/m106_mn01_n1_lrg_20150702_1150_pred_validated_ER_20150703"
)

#images = [gray2rgb(img) for img in reader.images]
images = reader.images

os.makedirs("/tmp/zooprocess")

print("Processing...")
for obj in reader():
    object_id = obj["object_id"]
    data = obj["facets"]["zooprocess"]["data"]
    roi = obj["facets"]["zooprocess"]["image"]
    print(object_id, data)
    x, y, w, h, idx, ident, item = (data[k] for k in (
        "BX", "BY", "Width", "Height", "Imageindex", "sorted_label", "!Item"))

    x, y, w, h, idx = int(x), int(y), int(w), int(h), int(idx)

    image = images[idx - 1]

    if idx == 1:
        # Save ROI
        imsave(
            "/tmp/zooprocess/{}-{}.png".format(idx - 1, item),
            roi
        )

    # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 4)
    # cv2.putText(image, "{:d}".format(item),
    #             (x + 10, y + 50), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 4)
    # # cv2.putText(image, ident,
    # #             (x + 10, y + 120), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 4)

# print("Saving...")
# x, y, w, h = 8648, 2246, 3715, 2786
# for i, img in enumerate(images):
#     imsave(
#         "/tmp/zooprocess-raw-{}.png".format(i),
#         img[y:y + h, x:x + w]
#     )
