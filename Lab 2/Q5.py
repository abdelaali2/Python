# Q5: Write a Python program that reads a file named example.txt and
# counts the number of lines in the file.

with open("Lab 2\Q5.txt") as myFile:
    print(len(myFile.readlines()))
