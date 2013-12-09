#! /usr/bin/env octave

a = str2double(getenv("a"));
b = str2double(getenv("b"));
dt = str2double(getenv("dt"));
tf = str2double(getenv("tf"));
y0 = str2double(getenv("y0"));

disp(glycolysis(0, y0, a, b, dt, tf));

