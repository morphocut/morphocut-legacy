import phasepack
from skimage import io
import matplotlib.pyplot as plt
import ftdetect.cleanedges as cleanedges
from skimage import filters
import numpy as np

img_fn = "/home/moi/Work/19-04-14 DF12 Morten Iversen/DF12/400m/IMG_6427.JPG"

img = io.imread(img_fn, as_gray=True)

img = img[500:1000, 3500:4000]

# TODO: You may want to experiment with the values of 'nscales' and 'k', the noise compensation factor.
M, m, ori, ft, PC, EO, T = phasepack.phasecong(img)

# TODO: M or M + m?
edges = M

# TODO: tlo, thi
edges_clean = cleanedges.hystThresh(edges)

fig, axes = plt.subplots(ncols=4, sharex=True, sharey=True)

axes[0].imshow(img)
axes[1].imshow(edges)
axes[3].imshow(edges_clean > 0)

# Experitur: start from single values for parameters and infer suitable range
# How to do that? -> p * [1 - epsilon, 1 + epsilon]
# jitter=True
# First pass: Record defaults
# Then: Create grid of jittered values


@Experiment
def baseline():
    ...


jitter_ex = baseline.child(...)  # or Experiment(parent=baseline, ...)


@jitter_ex.pre
def pre(...):
    epsilon = 0.1

    for params in grid:
        yield params
        # Run experiment once & record defaults
        # select only numeric parameters

        # Create grid from jittered values
        for params2 in grid2:
            yield {**params, params2}


hyperopt = baseline.child(...)


@hyperopt.pre
def hyperopt_pre():
    while n_experiments < max_experiments:
        # Train surrogate model with existing values (all compatible ones = same run method)
        # Predict next best parameter setting
        params = model.suggest()
        yield params
