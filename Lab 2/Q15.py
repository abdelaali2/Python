# Write a function that takes an arbitrary number of lists as input
# using *args and returns a new list that contains all the elements
# from all the input lists.

list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list3 = ["h", "i", "j"]


def combineLists(*args):
    finalList = []
    for arg in args:
        finalList += arg
    return finalList


print(f"The total list is: {combineLists(list1,list2,list3)}")
