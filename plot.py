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

for dt,eps in product((0.1,0.01,0.001), (0,0.1,5)):
    print("dt=%f, eps=%f" % (dt,eps))
    euler = call('bin/euler', dt=dt, eps=eps, p0=0.1)
    rk4 = call('bin/euler', dt=dt, eps=eps, p0=0.1)
    euler = np.loadtxt(StringIO(euler))
    rk4 = np.loadtxt(StringIO(rk4))

    print("plotting...")
    figure = plt.figure()
    axes = figure.add_subplot(111)
    figure.suptitle(r'$\Delta t=%f$, $\epsilon=%f$' % (dt, eps))

    axes.plot(euler[:,0], euler[:,1], label=r'$x_{\mathrm{eul}}$')
    axes.plot(euler[:,0], euler[:,2], label=r'$\dot{x}_{\mathrm{eul}}$')
    axes.plot(rk4[:,0], rk4[:,1], label=r'$x_{\mathrm{rk4}}$')
    axes.plot(rk4[:,0], rk4[:,2], label=r'$\dot{x}_{\mathrm{rk4}}$')

    axes.legend(loc='lower left')

    figure.savefig("dt=%f_eps=%f.png"%(dt,eps))
