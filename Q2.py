# Q2: Write a Python program that prompts the user to enter two 
# numbers and prints out their sum, difference, product, and 
# quotient.
# 

print ("Enter the first No.")
num1 = input()
num1 = int(num1)
print ("Enter the Second No.")
num2 = input()
num2 = int(num2)

def calculator(x,y):
    print(f'sum = { x + y }')
    print(f'sub = { x - y }')
    print(f'Mul = { x * y }')
    print(f'Div = { x / y }')
    print(f'Quotient = { x % y }')

calculator(num1,num2)