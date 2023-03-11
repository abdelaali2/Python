# Q1: Write a Python program that uses the math module to calculate
# the area of a circle with a radius of 5.

import math

print("Enter Radius: ")

rad = int(input())


def calcArea(r):
    return math.pi * pow(r, 2)


print("The area is: ", calcArea(rad))
