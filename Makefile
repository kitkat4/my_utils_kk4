TARGET = test_aa_utils.out

SRC := $(wildcard *.cpp)
OBJ := $(SRC:%.cpp=%.o)

.PHONY: all
all: $(TARGET)

%.out: $(OBJ)
	g++ -o $@ $^ 

%.o: %.cpp
	g++ -o $@ -c $^ 

