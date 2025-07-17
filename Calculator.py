number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    print(f"{number1} + {number2} = {number1 + number2}")
elif operator == "-":
    print(f"{number1} - {number2} = {number1 - number2}")
elif operator == "*":
    print(f"{number1} * {number2} = {number1 * number2}")
elif operator == "/":
    if number2 != 0:
        print(f"{number1} / {number2} = {number1 / number2}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operator")