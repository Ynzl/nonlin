all: euler rk4

euler: integrate.cpp integrate.h io.h
	g++ -std=c++11 $< -o $@ -DINTEGRATION_SCHEME=euler

rk4: integrate.cpp integrate.h io.h
	g++ -std=c++11 $< -o $@ -DINTEGRATION_SCHEME=rk4
