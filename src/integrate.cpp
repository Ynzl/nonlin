#include <iostream>
#include <iomanip>      // scientific, setprecision
#include "io.h"         // env, print
#include "integrate.h"  // euler, rk4

#ifndef INTEGRATION_SCHEME
# error Must compile with -DINTEGRATION_SCHEME=euler or rk4!
#endif

int main()
{
    using namespace std;
    using namespace io;

    typedef double
        Scalar, Time;

    typedef integrate::State<Scalar, Scalar>
        State;

    cout << scientific << setprecision(5);

    // initial values
    Time dt = env<Time>("dt", 0.1),
         tf = env<Time>("tf", 10);
    Scalar epsilon = env<Scalar>("eps", 0.1);
    State q(env<Scalar>("x0", 0),
            env<Scalar>("p0", 0));

    // state derivative (RHS of ODE)
    auto dq_dt =
        [epsilon] (State q, Time t)
    {
        return State(q.p, epsilon*(1-q.x*q.x)*q.p - q.x);
    };

    // integration
    print(cout, Time(0), q.x, q.p);
    for (Time t = 0; t <= tf; t += dt) {
        integrate::INTEGRATION_SCHEME(q, t, dt, dq_dt);
        print(cout, t, q.x, q.p);
    }

    return 0;
}

