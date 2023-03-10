# Q4: Write a Python program that prompts the user to enter their age 
# and prints out a message saying whether they are old enough to 
# vote (age 18 and above) or not.

print("Enter your age: ")
userInput = input()
userInput = int(userInput)

def validateAge(age):
    if (age >= 18):
        print("You're old enough to vote")
    else:
        print("You're not old enough to vote")

validateAge(userInput)
