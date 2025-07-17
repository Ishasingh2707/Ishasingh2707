gender = int(input("Enter a gender (1 for Male, 2 for Female): "))
age = int(input("Enter age: "))

if gender == 1:
    if age >= 21:
        print("You are eligible for marriage")
    else:
        print("You are not eligible for marriage")
elif gender == 2:
    if age >= 18:
        print("You are eligible for marriage")
    else:
        print("You are not eligible for marriage")
else:
    print("Invalid gender choice")