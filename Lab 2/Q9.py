# Q9: Write a Python program that reads a file named example.txt and
# prints the longest word in the file.

with open("Lab 2\Q9_Example.txt") as myFile:

    fileContent1 = myFile.read().split()
    longestWord = max(fileContent1, key=len)
    print(longestWord)
