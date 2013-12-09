#! /usr/bin/env bash

here=$(dirname $(readlink -nf "$BASH_SOURCE"))
mkdir -p $here/data

for dt in 0.1 0.01 0.001; do
    for eps in 0 0.1 5; do
        echo dt=$dt, eps=$eps
        dt=$dt eps=$eps $here/bin/rk4 >$here/data/rk4-dt=$dt-eps=$eps.txt
        dt=$dt eps=$eps $here/bin/euler >$here/data/euler-dt=$dt-eps=$eps.txt
    done
done

