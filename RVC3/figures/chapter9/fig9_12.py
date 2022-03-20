#!/usr/bin/env python3

import matplotlib.pyplot as plt
import rvcprint

import bdsim

import vloop_test
vloop_test.sim.set_options(hold=False)

vloop_test.bd['disturbance'].set_param('value', 40/107.815)
vloop_test.bd['VLOOP/Ki'].set_param('K', 2.0)
out = vloop_test.sim.run(vloop_test.bd, 1, dt=1e-3, watch=["demand[0]", "VLOOP/out[0]", "VLOOP/out[3]"])


plt.subplot(211)
plt.plot(out.t, out.y0, 'r', label='demand')
plt.plot(out.t, out.y1, 'b', label='actual')
plt.grid(True)
plt.xlim(0, 0.6)
plt.ylim(-5, 55)
plt.legend()
plt.ylabel(r'$\mathbf{\omega}\, (\mathrm{rad\,  s^{-1}})$')

plt.subplot(212)
plt.plot(out.t, out.y2, 'k')
plt.xlim(0, 0.6)
plt.ylim(0, 2)
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Integral value')

rvcprint.rvcprint()

