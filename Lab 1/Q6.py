# Q6: Write a Python program that prompts the user to enter a number
# and prints out a message saying whether the number is positive,
# negative, or zero.

print("Enter a Number")

userInput = input()
userInput = int(userInput)


def validateNumber(x):
    if x > 0:
        print("The Number is Positive")
    elif x < 0:
        print("The Number is Negative")
    elif x == 0:
        print("The Number equals Zero")


validateNumber(userInput)
