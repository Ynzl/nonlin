#! /usr/bin/env octave

a = str2double(getenv("a"));
b = str2double(getenv("b"));
dt = str2double(getenv("dt"));
tf = str2double(getenv("tf"));
p0 = str2double(getenv("p0"));

disp(glycolysis(0, p0, a, b, dt, tf));

