# Q10: Write a Python program that reads in a list of strings and prints
# out the strings in alphabetical order.

print("Enter the length of the list")

listLength = input()
listLength = int(listLength)

userInput = []

for i in range(listLength):

    print("Enter your string: ")
    inputValue = input()
    userInput.append(inputValue)

print("Your list is: ")
print(userInput)


def orderAlpha(list1):
    list1.sort()
    return list1


print("Your ordered list is: ")
print(orderAlpha(userInput))
