// Very Basic PNG Steganography
// By Andrew Player and Robert Lawton
// Fall 2020

#include <iostream>
#include <vector>
#include <stdio.h>
#include <fstream>

int main(int argc, char* argv[]) {
    if(argv[1] == nullptr) {
        std::cout << "ERROR: Please enter a valid filename" << std::endl;
        return 1;
    }

    if(argv[2] == nullptr) {
        std::cout << "Please Enter a Message: ";
        std::string message;
        std::getline(std::cin, message);
        std::ofstream out;
        out.open(argv[1], std::ios::app);
        out << message;
        return 0;
    }

    std::ofstream out;
    out.open(argv[1], std::ios::app);
    out << argv[2];

    return 0;
}
