import cv2
from skimage.feature import register_translation
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from skimage import img_as_float64

fnames = ["/data1/mschroeder/Datasets/18-10-SedimentTrap-Fred/M138 T4 600A/T4 600A 13.jpeg",
          "/data1/mschroeder/Datasets/18-10-SedimentTrap-Fred/M138 T4 600A/T4 600A 3.jpeg"]

frames = [cv2.imread(fn, cv2.IMREAD_GRAYSCALE) for fn in fnames]
frames = [2 * img_as_float64(f) - 1 for f in frames]

# Subpixel-accurate registration
# translation = register_translation(frames_pol[0][...,0], frames_pol[1][...,0])


def register_frames(frame1, frame2):
    def fitness(x):
        """
        x is a vector encoding angle and scale.
        """

        theta = np.rad2deg(np.arctan2(x[1], x[0]))
        scale = np.linalg.norm(x)
        #scale = 1

        print("Eval {!r} ({:.2f}° x{:.2f})...".format(x, theta, scale))

        rows, cols = frame2.shape
        M = cv2.getRotationMatrix2D((cols/2, rows/2), theta, scale)

        # print(M)

        # cos = np.abs(M[0, 0])
        # sin = np.abs(M[0, 1])
        # nrows = int((cols * sin) + (rows * cos))
        # ncols = int((cols * cos) + (rows * sin))

        template = cv2.warpAffine(frame2, M, (cols, rows))

        # cv2.imshow('template', template)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        shifts, error, phasediff = register_translation(frame1, template)

        M_trans = np.float32([[1, 0, shifts[1]], [0, 1, shifts[0]]])
        dst = cv2.warpAffine(template, M_trans, (cols, rows))

        blend = cv2.addWeighted(frame1 + 1, 0.25, dst + 1, 0.25, 0)

        cv2.imshow('blend', blend)
        cv2.imshow('frame1', (frame1 + 1) / 2)
        cv2.imshow('frame2', (template + 1) / 2)
        cv2.waitKey(100)

        print("", shifts, error)

        return error

    res = minimize(fitness, [0.16275058, 0.98666724], method='Nelder-Mead')
    print(res)

cv2.namedWindow('blend', cv2.WINDOW_NORMAL)
cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)
cv2.namedWindow('frame2', cv2.WINDOW_NORMAL)
try:
        register_frames(frames[0], frames[1])
finally:
        cv2.destroyAllWindows()