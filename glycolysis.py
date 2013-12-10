#! /usr/bin/env python

import os
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from subprocess import check_output


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

ti = 0
tf = 150
dt = 0.01
for b in np.linspace(0.0, 5, 10):
    print("b=%s" % b)
    params = dict(dt=dt, tf=tf, y0=0.1, a=0.04, b=b)
    glycos = numprog('octave', '-q', 'glycosolve.m', **params)

    # plot x(t), p(t)
    figure = plt.figure()
    axes = figure.add_subplot(111)
    figure.suptitle(r'$\Delta t=%s$, $b=%s$' % (dt, b))

    t = np.linspace(ti, tf, int((tf-ti)/dt))

    axes.plot(t, glycos[:,0], label=r'$x$')
    axes.plot(t, glycos[:,1], label=r'$y$')

    axes.legend(loc='lower left')
    figure.savefig("graph/glycolysis-time_b=%s.png"%(b))
    plt.close()

    # phase portrait:
    figure = plt.figure()
    axes = figure.add_subplot(111)
    figure.suptitle(r'Phase portrait for $\Delta t=%s$, $b=%s$' % (dt, b))
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.plot(glycos[:,0], glycos[:,1])
    figure.savefig("graph/glycolysis-phase_b=%s.png"%b)
    plt.close()


