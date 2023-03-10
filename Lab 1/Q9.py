# Q9: Write a Python function that takes a list of integers as input and
# returns a new list containing only the even numbers.

print("Enter the length of the list")

listLength = input()
listLength = int(listLength)

userInput = []

for i in range(listLength):

    print("Enter value")
    inputValue = input()
    inputValue = int(inputValue)
    userInput.append(inputValue)

print("Your list is: ")
print(userInput)


def getEvenFromList(myList):
    newList = []
    for i in range(listLength):
        if myList[i] % 2 == 0:
            newList.append(myList[i])
    return newList


print("The even values in your list are: ")
print(getEvenFromList(userInput))
