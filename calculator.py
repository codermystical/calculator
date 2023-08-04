#this program is a simple calculator
import math

#Welcome message
print(" Welcome to Brandon's Basic Calculator :-)")

#Accounts for the addition
def add(x, y):
    return x + y

#Accounts for the subtraction
def subtract(x, y):
    return x - y

#Accounts for multiplication
def multiply(x, y):
    return x * y

#Accounts for division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        print('Cant divide by 0, sorry!')

#Creats the list of math sequences to choose from
while True:
    print('''
    Option 1: Addition
    Option 2: Subtraction
    Option 3: Multiplication
    Option 4: Division
    Option 5: Exit''')

    #If the exit option is clicked than the user will be directed out
    mathChoice = int(input("Pick a math option > "))
    if mathChoice == 5:
        exit()
    break



#Will ask the user for the numbers wanted to be used in the calculations
choice1 = float(input("Choose your first number > "))
choice2 = float(input("Choose your second number > "))

#Does calculations
if mathChoice == 1:
    print(add(choice1,choice2))
elif mathChoice == 2:
    print(subtract(choice1,choice2))
elif mathChoice == 3:
    print(multiply(choice1,choice2))
elif mathChoice == 4:
    print(divide(choice1,choice2))
else:
    print("Invalid :(")

#Will repeat the code if they want to preform another calculation
def myRepeatedCode():
    print(" Welcome to Brandon's Basic Calculator :-)")

    # Accounts for the addition
    def add(x, y):
        return x + y

    # Accounts for the subtraction
    def subtract(x, y):
        return x - y

    # Accounts for multiplication
    def multiply(x, y):
        return x * y

    # Accounts for division
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            print('Cant divide by 0, sorry!')

    # Creates the list of math sequences to choose from
    while True:
        print('''
        Option 1: Addition
        Option 2: Subtraction
        Option 3: Multiplication
        Option 4: Division
        Option 5: Exit''')

        # If the exit option is clicked than the user will be directed out
        mathChoice = int(input("Pick a math option > "))
        if mathChoice == 5:
            exit()
        break

    # Will ask the user for the numbers wanted to be used in the calculations
    choice1 = float(input("Choose your first number > "))
    choice2 = float(input("Choose your second number > "))

    # Does calculations
    if mathChoice == 1:
        print(add(choice1, choice2))
    elif mathChoice == 2:
        print(subtract(choice1, choice2))
    elif mathChoice == 3:
        print(multiply(choice1, choice2))
    elif mathChoice == 4:
        print(divide(choice1, choice2))
    else:
        print("Invalid :(")

repeat = input("Would you like to preform another calculation? (yes or no) > ")

if repeat == "yes":
    myRepeatedCode()
else:
    print("Goodbye :)")





