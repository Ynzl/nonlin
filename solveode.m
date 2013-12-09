function x = solveode(eps, dt=0.1, tmax=20)
    xinit = [0, 0.1];
    t = linspace(0, tmax, tmax / dt + 1)';

    xdot = @(x,t) [x(2), eps * (1 - x(1)**2) * x(2) - x(1)];

    x = lsode(xdot, xinit, t);
    plot(t,x);
endfunction
