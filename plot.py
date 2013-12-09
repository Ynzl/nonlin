#! /usr/bin/env python

import os
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from subprocess import check_output
from itertools import product


def call(*args, **kwargs):
    return check_output(
        ['env'] + ['%s=%s'%(k,str(v)) for k,v in kwargs.items()] + list(args)
    ).decode('utf-8')

try:
    os.makedirs('graph')
except IOError:
    pass

for dt,eps in product((0.1,0.01,0.001), (0,0.1,5)):
    print("dt=%s, eps=%s" % (dt,eps))
    euler = call('bin/euler', dt=dt, eps=eps, p0=0.1, tf=20)
    rk4 = call('bin/rk4', dt=dt, eps=eps, p0=0.1, tf=20)
    euler = np.loadtxt(StringIO(euler))
    rk4 = np.loadtxt(StringIO(rk4))

    # plot x(t), p(t)
    figure = plt.figure()
    axes = figure.add_subplot(111)
    figure.suptitle(r'$\Delta t=%s$, $\epsilon=%s$' % (dt, eps))

    axes.plot(euler[:,0], euler[:,1], label=r'$x_\mathrm{eul}$')
    axes.plot(euler[:,0], euler[:,2], label=r'$\dot{x}_\mathrm{eul}$')
    axes.plot(rk4[:,0], rk4[:,1], label=r'$x_\mathrm{rk4}$')
    axes.plot(rk4[:,0], rk4[:,2], label=r'$\dot{x}_\mathrm{rk4}$')

    axes.legend(loc='lower left')
    figure.savefig("graph/time-evolution_dt=%s_eps=%s.png"%(dt,eps))

    # phase portrait:
    figure = plt.figure()
    axes = figure.add_subplot(111)
    figure.suptitle(r'Phase portrait for $\Delta t=%s$, $\epsilon=%s$' % (dt, eps))
    axes.plot(rk4[:,1], rk4[:,2], label=r'$x_\mathrm{eul}$')
    figure.savefig("graph/phase-portrait_dt=%s_eps=%s.png"%(dt,eps))


