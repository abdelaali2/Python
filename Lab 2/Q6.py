# Q6: Write a Python program that reads a file named example.txt and
# prints the contents of the file in reverse order.

from Q2_My_Module import reverseString

with open("Lab 2\Q6_Example.txt") as myFile:
    print(reverseString(myFile.read()))
