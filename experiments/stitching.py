import cv2
from skimage.feature import register_translation
import numpy as np
import matplotlib.pyplot as plt

fnames = ["/data1/mschroeder/Datasets/18-10-SedimentTrap-Fred/M138 T4 600A/T4 600A 13.jpeg",
          "/data1/mschroeder/Datasets/18-10-SedimentTrap-Fred/M138 T4 600A/T4 600A 3.jpeg"]

frames = [cv2.imread(fn) for fn in fnames]

frames_pol = []
for f in frames:
    print(f.shape)
    center = f.shape[0] / 2, f.shape[1] / 2
    frames_pol.append(cv2.warpPolar(f, (0, 0), center, max(
        center), cv2.WARP_POLAR_LOG + cv2.WARP_FILL_OUTLIERS))

for f in frames_pol:
    print(f.shape)

# Subpixel-accurate registration
# translation = register_translation(frames_pol[0][...,0], frames_pol[1][...,0])

image_product = np.fft.fft2(frames_pol[0][...,0]) * np.fft.fft2(frames_pol[1][...,0]).conj()
cc_image = np.fft.fftshift(np.fft.ifft2(image_product))
plt.imshow(cc_image.real)