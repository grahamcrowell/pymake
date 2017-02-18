# http://mrbook.org/blog/tutorials/make/

VPATH = ../../util/

all: main

main: main.o path.o
	g++ $^ -o $@

path.o: path.cpp
	g++ -c path.cpp

main.o: main.cpp
	g++ -c main.cpp

clean:
	rm *o main
