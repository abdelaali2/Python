# Q16: Write a function that takes a string as input and an arbitrary
# number of keyword arguments using **kwargs. The function should
# replace all instances of the keyword argument keys in the input
# string with their corresponding values.

string = "name: "


def swapFromKWARGS(string1, **kwargs):
    for value in kwargs.values():
        string1 += value
    return string1


print(swapFromKWARGS(string, firstName="Ibrahim ", lastName="Badr"))
