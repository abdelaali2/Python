# Q14: Write a function that takes a list of numbers as input and
# returns a new list containing the squares of each number in the
# input list.

import math

print("Enter the length of the list")

listLength = int(input())
userInput = []

for i in range(listLength):

    print("Enter value")
    inputValue = int(input())
    userInput.append(inputValue)

print(f"Your list is:\n {userInput}")


def getSquared(lst):
    newList = []
    for num in lst:
        newList.append(pow(num, 2))
    return newList


print(f"Here's your list squared:\n{getSquared(userInput)}")
