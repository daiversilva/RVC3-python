#!/usr/bin/env python3

import rvcprint
import numpy as np
import matplotlib.pyplot as plt
from machinevisiontoolbox import *
from matplotlib.ticker import ScalarFormatter
from matplotlib import cm

if '_rvcprint' in globals():
    doprint = _rvcprint
else:
    doprint = True

# load linear color image
im_targets = Image.Read('yellowtargets.png', dtype='float', gamma='sRGB')
im_targets.disp()
if doprint:
    rvcprint.rvcprint(subfig='a')

# ensure consistent k-means clustering
#  seed OpenCV's random number generator (RNG)
cv.setRNGSeed(0)

k = 2

ab = im_targets.colorspace('Lab').plane('ab')

labels, centres, _ = ab.colorkmeans(k)
labels.disp(ncolors=k, colormap='jet', colorbar=True)
if doprint:
    rvcprint.rvcprint(subfig='b')

plt.clf()
plot_chromaticity_diagram(colorspace='ab')
plot_point(centres.T, marker='*', text='{}')
if doprint:
    rvcprint.rvcprint(subfig='c')

objects = (labels == 0)
objects.disp(black=0.3)
if doprint:
    rvcprint.rvcprint(subfig='d')

targets_binary = objects.open(Kernel.Circle(2))
targets_binary.disp(black=0.3)
if doprint:
    rvcprint.rvcprint(subfig='e')

if doprint:
    plt.close('all')
    plt.show()
