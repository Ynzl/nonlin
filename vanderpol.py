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

def numprog(*args, **kwargs):
    return np.loadtxt(StringIO(call(*args, **kwargs)))

try:
    os.makedirs('graph')
except OSError:
    pass

for dt,(eps,tf) in product((0.1,0.01,0.001), ((0,30),(0.1,100),(5,30))):
    print("dt=%s, eps=%s" % (dt,eps))
    params = dict(dt=dt, eps=eps, p0=0.1, tf=tf)
    eul = numprog('bin/euler', **params)
    rk4 = numprog('bin/rk4', **params)
    octave = numprog('octave', '-q', 'vandersolve.m', **params)
    m = min(len(eul), len(rk4), len(octave))

    # plot x(t), p(t)
    figure = plt.figure()
    axes = figure.add_subplot(111)
    figure.suptitle(r'$\Delta t=%s$, $\epsilon=%s$' % (dt, eps))

    axes.plot(eul[:,0], eul[:,1], label=r'$x_\mathrm{eul}$')
    axes.plot(eul[:,0], eul[:,2], label=r'$\dot{x}_\mathrm{eul}$')
    axes.plot(rk4[:,0], rk4[:,1], label=r'$x_\mathrm{rk4}$')
    axes.plot(rk4[:,0], rk4[:,2], label=r'$\dot{x}_\mathrm{rk4}$')

    axes.legend(loc='lower left')
    figure.savefig("graph/time-evolution_dt=%s_eps=%s.png"%(dt,eps))
    plt.close()
    
    figure = plt.figure()
    axes = figure.add_subplot(111)
    figure.suptitle(r'$\Delta t=%s$, $\epsilon=%s$' % (dt, eps))

    axes.plot(eul[:m,0], octave[:,0], label=r'$x_\mathrm{lsode}$')
    axes.plot(eul[:m,0], octave[:,1], label=r'$\dot{x}_\mathrm{lsode}$')

    axes.legend(loc='lower left')
    figure.savefig("graph/time-evolution-lsode_dt=%s_eps=%s.png"%(dt,eps))
    plt.close()


    # error plot:
    figure = plt.figure()
    axes = figure.add_subplot(111)
    figure.suptitle(r'$\Delta t=%s$, $\epsilon=%s$' % (dt, eps))
    err_eul = abs(eul[:m,1] - octave[:m,0])
    err_rk4 = abs(rk4[:m,1] - octave[:m,0])
    axes.plot(eul[:m,0], err_eul, label=r'$\mathrm{err}_\mathrm{eul}$')
    axes.plot(eul[:m,0], err_rk4, label=r'$\mathrm{err}_\mathrm{rk4}$')
    axes.legend(loc='lower left')
    figure.savefig("graph/error_dt=%s_eps=%s.png"%(dt,eps))
    plt.close()

    # phase portrait:
    figure = plt.figure()
    axes = figure.add_subplot(111)
    figure.suptitle(r'Phase portrait for $\Delta t=%s$, $\epsilon=%s$' % (dt, eps))
    axes.plot(rk4[:,1], rk4[:,2], label=r'$x_\mathrm{eul}$')
    figure.savefig("graph/phase-portrait_dt=%s_eps=%s.png"%(dt,eps))
    plt.close()


