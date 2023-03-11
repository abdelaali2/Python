# Q11: Write a function that takes a list of strings as input and returns a
# new list containing only the strings that start with the letter "a".

print("Enter the length of the list")

listLength = int(input())
userInput = []

for i in range(listLength):

    print("Enter value")
    inputValue = input()
    userInput.append(inputValue)

print(f"Your list is:\n {userInput}")


def startsWithA(lst):
    newlst = []
    for word in lst:
        if word.startswith("a") or word.startswith("A"):
            newlst.append(word)
    return newlst


print(f"The words that starts with A or a are:\n{startsWithA(userInput)}")
