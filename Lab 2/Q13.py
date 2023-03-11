# Q13: Write a function that takes a list of numbers as input and
# returns the largest and smallest numbers in the list.

print("Enter the length of the list")

listLength = int(input())
userInput = []

for i in range(listLength):

    print("Enter value")
    inputValue = int(input())
    userInput.append(inputValue)

print(f"Your list is:\n {userInput}")


def getMaxAndMin(lst):
    max = 0
    min = lst[0]
    for num in lst:
        if num > max:
            max = num
        elif num < min:
            min = num
    return print(f"Max value = {max}\nMin value = {min}")


getMaxAndMin(userInput)
