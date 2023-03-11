# Q10: Write a function that takes a list of integers as input and returns
# the sum of all even numbers in the list.

print("Enter the length of the list")

listLength = int(input())
userInput = []

for i in range(listLength):

    print("Enter value")
    inputValue = int(input())
    userInput.append(inputValue)

print(f"Your list is:\n {userInput}")


def sumOfEven(lst):
    sum = 0
    for value in lst:
        if value % 2 == 0:
            sum += value
    return sum


print(f"Sum of the even numbers in your list is: {sumOfEven(userInput)}")
