#!/usr/bin/env python3

import rvcprint
import numpy as np
import matplotlib.pyplot as plt
from machinevisiontoolbox import *
from matplotlib.ticker import ScalarFormatter
from matplotlib import cm
from spatialmath import base

sharks = Image.Read('sharks.png')

labels, n = sharks.labels_binary()
blob = labels == 3

blob.disp(black=0.3, grid=True)
uv = blob.nonzero()

umin = uv[0, :].min()
umax = uv[0, :].max()
vmin = uv[1, :].min()
vmax = uv[1, :].max()

plot_box('g', l=umin, t=vmin, r=umax, b=vmax)

moments = blob.moments()
print(moments)

m00 = moments['m00']
uc = moments['m10'] / m00
vc = moments['m01'] / m00
plot_point((uc, vc), marker=['ok', 'xk'], markerfacecolor='none')

u20 = moments['mu20']
u02 = moments['mu02']
u11 = moments['mu11']
J = np.array([[u20, u11], [u11, u02]])
lmbda, x = np.linalg.eig(J)
ab = 2 * np.sqrt(lmbda / m00)
print(ab[0] / ab[1])
print('eigs', lmbda)
print('eigval', x)
v = x[:, 0]
math.atan2(v[1], v[0])

base.plot_ellipse(4 * J / m00, [uc, vc], inverted=True, color='b', linewidth=2)

rvcprint.rvcprint(subfig='a')


plt.xlim(400, 600)
plt.ylim(300, 100)
rvcprint.rvcprint(subfig='b', thicken=2)
