#ifndef __INTEGRATE_H__INCLUDED__
#define __INTEGRATE_H__INCLUDED__

#include <boost/operators.hpp>
#include <cmath>    // std::abs, std::pow

namespace integrate
{

    template <class S,
              class Q,
              class P = Q>
    struct State
        : boost::addable< State<S,Q,P>
        , boost::multipliable< State<S,Q,P>, S
        , boost::dividable< State<S,Q,P>, S
        > > >
    {
        typedef S Scalar;
        typedef Q Position;
        typedef P Momentum;

        State(const Position& x, const Momentum& p)
            : x(x)
            , p(p)
        {
        }

        Position x;
        Momentum p;

        State& operator += (const State& s) {
            x += s.x;
            p += s.p;
            return *this; }

        State& operator *= (const Scalar& s) {  // used in derivation context
            x *= s;
            p *= s;
            return *this; }

        State& operator /= (const Scalar& s) {
            return *this *= (1/s); }
    };

    /*
     * integration schemes
     */

    template <class Q, class T, class D>    // Q: state, T: time, D: derivation operator
    void rk4(Q& q, T t, T dt, D dQ)         // dQ(q,t) is actually dq/dt (t)
    {
        Q a(dt*dQ(q, t)),
          b(dt*dQ(q + a/2, t + dt/2)),
          c(dt*dQ(q + b/2, t + dt/2)),
          d(dt*dQ(q + c, t+dt));
        q += (a + 2*(b + c) + d)/6;
    }

    template <class Q, class T, class D>
    void euler(Q& q, T t, T dt, D dQ)
    {
        q += dQ(q, t) * dt;
    }

} // ns integrate

#endif // include guard

