// Very Basic PNG Steganography
// By Andrew Player and Robert Lawton
// Fall 2020

#include <iostream>
#include <vector>
#include <stdio.h>
#include <fstream>

// Usage:
//
// For best results, the message should be hidden in a png file.
// The message is simply concatenated to the end of the file.
//
// Use Case 1:
// ./steg.exe filename "message"
//
// Use Case 2:
// ./steg.exe filename
// Please Enter a Message: "message"
//
//Use Case 3:
// cat message.txt | ./steg.exe filename

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
