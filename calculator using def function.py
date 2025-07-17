# Define functions for calculator
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# User options that should be performes
print("""Enter operation to be performed
1 for add
2 for sub
3 for mul
4 for div""" )

# Take user input
c = input("Enter your choice--> ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# function calling
if c == "1":
    print("Addition of two numbers:", add(num1, num2))
elif c == "2":
    print("Subtraction of two numbers:", sub(num1, num2))
elif c == "3":
    print("Multiplication of two numbers:", mul(num1, num2))
elif c == "4":
    if num2 != 0:
        print("Division of two numbers:", div(num1, num2))
    else:
        print("Cannot divide by zero!")
else:
    print("You entered a wrong operation!!!")