# Q2: Create a custom Python module called my_module with a
# function that takes a string as input and returns the reverse of the
# string. Then write a Python program that imports the my_module
# module and uses the reverse_string function to reverse the string
# "Hello, world!".

import Q2_My_Module as customModule

print("Enter your string: ")
inp = input()

print("The reversed string is: ")
print(customModule.reverseString(inp))