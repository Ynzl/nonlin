all: bin/euler bin/rk4

clean:
	rm -rf bin/*

bin/%: src/integrate.cpp src/integrate.h src/io.h
	@mkdir -p bin
	g++ -std=c++11 $< -o $@ -DINTEGRATION_SCHEME=$* -O3

