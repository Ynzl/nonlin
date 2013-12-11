function x = glycolysis(x0, y0, a, b, dt=0.1, tmax=30)
    xinit = [x0, y0];
    t = linspace(0, tmax, tmax / dt);

    xdot = @(x,t) [a*x(2) + x(2)*x(1)**2 - x(1),
                   -a*x(2) - x(2)*x(1)**2 + b];

    x = lsode(xdot, xinit, t);
    plot(t,x)
endfunction
