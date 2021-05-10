#!/usr/bin/env python3

import rvcprint
import numpy as np
import matplotlib.pyplot as plt
from machinevisiontoolbox import *
from matplotlib.ticker import ScalarFormatter
from matplotlib import cm


b1 = Image.Read('building2-1.png', grey=True, dtype='float')
pks, _ = b1.harriscorner(nfeat=200, hw=2, scale=7)

s = pks[:, 2]
print(len(s), ' features returned')

h, x = np.histogram(pks[:, 2], 100)
cdf = np.cumsum(h)
cdf = cdf / cdf[-1]
plt.bar(x[1:], cdf, width=x[1]-x[0])
print(x)

# histogram(s(:), 'Normalization', 'cdf', 'EdgeColor', 'none')
# #xaxis(max(x)) yaxis(0.8, 1)
# yaxis(0.5, 1)
ylim = plt.gca().get_ylim()
plt.plot(np.r_[1, 1] * x[-1] / 2, ylim, 'r--')
plt.xlabel('Corner strength')
plt.xlim(0, x[-1])
plt.ylim(0, 1)
plt.ylabel('Cumulative number of features')
plt.grid(True)
#(1-interp1(x, ch, strongest/2))*100

rvcprint.rvcprint()


