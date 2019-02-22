import cv2
from skimage.feature import register_translation
#from skimage.feature import masked_register_translation
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from skimage.filters import threshold_otsu
from skimage import img_as_ubyte
from skimage import img_as_float64

fnames = ["/data1/mschroeder/Datasets/18-10-SedimentTrap-Fred/M138 T4 600A/T4 600A 13.jpeg",
          "/data1/mschroeder/Datasets/18-10-SedimentTrap-Fred/M138 T4 600A/T4 600A 3.jpeg"]

frames = [cv2.imread(fn, cv2.IMREAD_GRAYSCALE) for fn in fnames]

# Convert range to (-1,1)
frames = [2 * img_as_float64(f) - 1 for f in frames]

# Subpixel-accurate registration
# translation = register_translation(frames_pol[0][...,0], frames_pol[1][...,0])

def matmul(A, B):
    Ah = np.eye(3)
    Bh = np.eye(3)

    Ah[:2] = A
    Bh[:2] = B

    print(Ah)
    print(Bh)
    
    result = np.matmul(Ah, Bh)

    print(result)

    return result[:2]


def register_frames(frame1, frame2):
    trials = []
    def fitness(theta):
        """
        x is a vector encoding angle and scale.
        """

        scale = 1

        print("Eval {:.2f}° x{:.2f}...".format(theta, scale))

        rows, cols = frame2.shape
        M = cv2.getRotationMatrix2D((cols/2, rows/2), theta, scale)

        # print(M)

        # cos = np.abs(M[0, 0])
        # sin = np.abs(M[0, 1])
        # nrows = int((cols * sin) + (rows * cos))
        # ncols = int((cols * cos) + (rows * sin))

        template = cv2.warpAffine(frame2, M, (cols, rows))
        # dst_mask = cv2.warpAffine(np.ones_like(frame2, dtype=bool), M, (cols, rows), None, cv2.INTER_NEAREST)

        # cv2.imshow('template', template)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        thr1 = threshold_otsu(frame1)
        thr2 = threshold_otsu(frame2)

        bw1 = frame1 < thr1
        bw2 = template < thr2

        shifts, error, phasediff = register_translation(frame1, template)

        # src_mask = np.ones_like(frame1, dtype=bool)
        # masked_register_translation(frame1, template, )

        M_trans = np.float32([[1, 0, shifts[1]], [0, 1, shifts[0]]])

        M_combined = matmul(M_trans, M)

        dst2 = cv2.warpAffine(frame2, M_combined, (cols, rows))

        blend2 = cv2.addWeighted(frame1 + 1, 0.25, dst2 + 1, 0.25, 0)

        cv2.imshow('blend2', blend2)
        cv2.imshow('frame1', (frame1 + 1) / 2)
        cv2.imshow('frame2', (template + 1) / 2)
        cv2.waitKey(100)

        print("", shifts, error)

        trials.append(M_combined, error)

        return error

    angles = np.arange(0,360)
    errors = np.zeros_like(angles, dtype=float)
    for i, angle in enumerate(angles):
        errors[i] = fitness(angle)

    plt.plot(angles, errors)

    return errors

cv2.namedWindow('blend2', cv2.WINDOW_NORMAL)
cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)
cv2.namedWindow('frame2', cv2.WINDOW_NORMAL)
try:
    errors = register_frames(frames[0], frames[1])
finally:
    cv2.destroyAllWindows()
