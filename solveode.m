function x = solveode(x0, p0, eps, dt=0.1, tmax=30)
    xinit = [x0, p0];
    t = linspace(0, tmax, tmax / dt);

    xdot = @(x,t) [x(2), eps * (1 - x(1)**2) * x(2) - x(1)];

    x = lsode(xdot, xinit, t);
endfunction
