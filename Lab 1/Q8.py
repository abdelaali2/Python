# Q8: Write a Python program that prompts the user to enter a sentence
# and prints out the sentence in all uppercase letters.

print("Enter your string: ")

userInput = input()


def toUpper(str):
    return str.upper()


print(toUpper(userInput))
