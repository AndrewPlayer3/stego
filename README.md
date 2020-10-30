# Steganography Project for CS 465

Usage:
For best results, the message should be hidden in a png file.
The message is simply concatenated to the end of the file.

Use Case 1:
./steg.exe filename "message"

Use Case 2:
./steg.exe filename
Please Enter a Message: "message"

Use Case 3:
cat message.txt | ./steg.exe filename

To Read the Message:
hexdump -C filename
