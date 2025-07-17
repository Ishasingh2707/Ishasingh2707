# Q:1 Create a  function greet(name) that prints"Hello, [name]!"
def greet(name):
    print(f"Hello, {name}!")
greet('Isha')


# Q:2 Create a function add(a,b) that returns the sum of two numbers. Call the function witth inputs.
def add(a, b):
    return a + b
r= add(10,5)
print(r )


# Q:3  Create a function display(*args) that accepts multiiple arguents and prints them.
def display(*args):
    print(args)
display("apple", "banana", "kivi")



# Q:4 Create a function
#student_info(**kwargs) that accepts name,age,roll number as keyword arguments and prints them.
def student_info(name, age, rollnumber):
    print("Name:", name)
    print("Age:", age)
    print("Roll Number:", rollnumber)
student_info(name="Isha", age=19, rollnumber=230624)