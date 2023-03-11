# Q7: Write a Python program that reads a file named example.txt and
# removes all newline characters from the file.

with open("Lab 2\Q7_Example.txt") as myFile:
    print(myFile.read().replace("\n", " -- "))
