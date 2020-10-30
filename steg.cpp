#include <iostream>
#include <vector>
#include <stdio.h>
#include <fstream>

int main(int argc, char* argv[]) {
    if(argv[1] == nullptr) {
        std::cout << "ERROR: Please enter a valid filename" << std::endl;
        return 1;
    }
    
    std::ofstream out;
    out.open(argv[1], std::ios::app);
    out << argv[2];
    
}

