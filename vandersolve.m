#! /usr/bin/env octave

eps = str2double(getenv("eps"));
dt = str2double(getenv("dt"));
tf = str2double(getenv("tf"));
p0 = str2double(getenv("p0"));

disp(vanderpol(0, p0, eps, dt, tf));

