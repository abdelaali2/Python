# Q8: Write a Python program that reads a file named example.txt and
# writes its contents to a new file named copy. txt.

destFile = open("Lab 2\Q8_Copy.txt", "w")

with open("Lab 2\Q8_Example.txt") as srcFile:
    destFile.writelines(srcFile.read() + "\n Copied by Ibrahim Badr")

destFile.close()

with open("Lab 2\Q8_Copy.txt") as myFile:
    print(myFile.read())
