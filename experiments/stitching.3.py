import cv2
from skimage.feature import register_translation
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from skimage import img_as_float64
from skimage.filters import gaussian

fnames = ["/data1/mschroeder/Datasets/18-10-SedimentTrap-Fred/M138 T4 600A/T4 600A 13.jpeg",
          "/data1/mschroeder/Datasets/18-10-SedimentTrap-Fred/M138 T4 600A/T4 600A 3.jpeg"]

frames = [cv2.imread(fn, cv2.IMREAD_GRAYSCALE) for fn in fnames]
frames = [img_as_float64(f) for f in frames]

frames_mean = np.array(frames).mean(axis=0)

frames_mean = gaussian(frames_mean, 200)

cv2.namedWindow('mean', cv2.WINDOW_NORMAL)
cv2.imshow('mean', frames_mean)
cv2.waitKey(0)
cv2.destroyAllWindows()

frames = [f / frames_mean for f in frames]

for i, f in enumerate(frames):
    title = 'frame{}'.format(i)
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.imshow(title, f)

cv2.waitKey(0)
cv2.destroyAllWindows()

def register_frames(frame1, frame2):
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
        dst_mask = cv2.warpAffine(np.ones_like(frame2, dtype=bool), M, (cols, rows), None, cv2.INTER_NEAREST)

        # cv2.imshow('template', template)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        #shifts, error, phasediff = register_translation(frame1, template)

        src_mask = np.ones_like(frame1, dtype=bool)
        masked_register_translation(frame1, template, )

        M_trans = np.float32([[1, 0, shifts[1]], [0, 1, shifts[0]]])
        dst = cv2.warpAffine(template, M_trans, (cols, rows))

        blend = cv2.addWeighted(frame1, 0.5, dst, 0.5, 0)

        print(np.min(frame1), np.max(frame1))
        print(np.min(dst), np.max(dst))
        print(np.min(blend), np.max(blend))

        cv2.imshow('blend', blend)
        #cv2.imshow('frame1', frame1)
        #cv2.imshow('frame2', dst)
        cv2.waitKey(100)

        print("", shifts, error)

        return error

    errors = np.empty(360)
    for theta in range(len(errors)):
        errors[theta] = fitness(theta)

cv2.namedWindow('blend', cv2.WINDOW_NORMAL)
cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)
cv2.namedWindow('frame2', cv2.WINDOW_NORMAL)
try:
    #register_frames(frames[0], frames[1])
    pass
finally:
    cv2.destroyAllWindows()
