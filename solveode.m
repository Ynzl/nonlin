function x = solveode(e)

xdot = @(x,t,e)[x(2),e*(1-x(1)*x(1))*x(2) - x(1)];

xinit = [0, 0.1];
t = linspace(0, 50, 100);

g = @(x,t) xdot(x,t,e);

x = lsode(g, xinit, t);
plot(t,x);
