# Q5: Write a Python function that takes a list of strings as input and
# returns the string with the most characters.

list1 = ["abc", "abcde", "abcdefgh", "abcde", "abc"]


def getLongest(inputList):
    return max(inputList, key=len)


print("The longest value is ", getLongest(list1))
