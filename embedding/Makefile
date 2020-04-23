CXX = g++
CXXFLAGS = --std=c++11 -Wall -Wno-sign-compare -Wno-unknown-pragmas -fPIC -fopenmp -O3 -pthread
INCLUDES = -I"/usr/include/"

all: PFNE

PFNE: PFNE.cpp docopt.o
	$(CXX) $(CXXFLAGS) $(INCLUDES) docopt.o PFNE.cpp -o PFNE
docopt.o: docopt.cpp/docopt.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c docopt.cpp/docopt.cpp -o docopt.o
check-syntax:
	$(CXX) -o nul $(CXXFLAGS) $(INCLUDES) -S PFNE.cpp

.PHONY : clean

clean:
	rm *.o PFNE
