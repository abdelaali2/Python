# Q7: Write a Python function that takes a string as input and returns the
# number of vowels in the string.

print("Enter your string: ")

userInput = input()

counter = 0


def countVowels(inputString):
    length = len(inputString)
    global counter

    for i in range(length):
        if inputString[i] in "aAeEiIoOuU":
            counter += 1

    return counter


print("The No. of vowels in your input is: ", countVowels(userInput))
