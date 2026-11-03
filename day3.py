#Day 3: Functions, parameters, return values, scope, type hints, docstrings and modules/imports.


from math import sqrt, pow #math is a built-in module that provides mathematical functions and constants. sqrt() calculates the square root of a number, and pow() raises a number to a specified power.



#Functions-Write the logic once and reuse it wherever needed.
def calculate_average(marks):
    return sum(marks) / len(marks)

print(calculate_average([80, 90, 100]))  # 90.0
print(calculate_average([60, 70, 80]))   # 70.0

#Parameter: A variable defined in the function declaration.
#Argument: The actual value passed when calling the function.

def hello(name):       # name is a parameter
    print(f"Hello, {name}!")

hello("Shobhit")       # "Shobhit" is an argument

#Types of arguments:
#1. Positional arguments-passed in the order of parameters defined in the function.
def subtract(a, b):
    return a - b

print(subtract(10, 3))  # 7

#2. Keyword arguments-passed by specifying the parameter name.
print(subtract(a=10, b=3))  # 7
print(subtract(b=3, a=10))  # 7

#3. Default arguments-values assigned to parameters in the function definition.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Shobhit")  # Hello, Shobhit!
greet("Shobhit", "Hi")  # Hi, Shobhit!

#4. Variable-length arguments
def sum_numbers(*numbers):
    return sum(numbers)

print(sum_numbers(1, 2, 3))  # 6
print(sum_numbers(4, 5, 6, 7))  # 22
#*numbers collects all positional arguments into a tuple named numbers called *args
#**kwargs collects all keyword arguments into a dictionary named kwargs

#Return values: A function can return a value using the return statement.
def multiply(a, b):
    return a * b

print(multiply(5, 3))  # 15

#Compare with print()
def add(a, b):
    return a + b

def add_and_print(a, b):
    print(a + b)

result = add(2, 3)          # result is 5
another_result = add_and_print(2, 3)  # prints 5
print(another_result)       # None

#Multiple return values
#Python can return multiple values in a tuple:
def calculate(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

total, average = calculate([80, 90, 100])

print(total)    # 270
print(average)  # 90.0


#Scope: The scope of a variable determines where it can be accessed in the code.
#1. Local scope: Variables defined inside a function are local to that function.
def my_function():
    local_var = 10  # Local variable
    return local_var

print(my_function())  # 10
#print(local_var)     # Error: local_var is not defined

#2. Global scope: Variables defined outside any function are global and can be accessed anywhere in the module.
global_var = 20  # Global variable

def my_function():
    return global_var

print(my_function())  # 20
print(global_var)     # 20

#Type hints: Type hints are optional annotations that specify the expected types of function parameters and return values.
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 3))  # 8

#Docstrings: Docstrings are multi-line strings used to document functions, classes, and modules.
def calculate_average(marks: list[float]) -> float:
    """Return the average of a non-empty list of marks."""
    return sum(marks) / len(marks)

print(calculate_average.__doc__) #Return the average of a non-empty list of marks and print the docstring
help(calculate_average)  # Displays the docstring and function signature


#Modules and imports: A module is a file containing Python code that can be imported and used in other Python files. You can import specific functions or classes from a module, or import the entire module.
#Importing specific functions from a module


print(sqrt(16))  # 4.0
print(pow(2, 3))  # 8.0


#Nested functions: Functions can be defined inside other functions. The inner function can access variables from the outer function's scope.
for s in range(3):
    for p in range(2):
        print(s, p)


#Generator Functions: A generator function is a special type of function that returns an iterator. It uses the yield statement to produce a series of values over time, instead of returning a single value and exiting.
#Stores one item in mem at a time.
#Computes values when explicitly requested.
#can easily maintain state between calls.
#can support infinite sequences.
def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count  # Pauses here and returns the current count
        count += 1   # Resumes here on the next call

# 1. Using a for loop
counter = count_up_to(3)
for num in counter:
    print(num)
# Output:
# 1
# 2
# 3

# 2. Manual iteration using next()
counter2 = count_up_to(2)
print(next(counter2))  # Output: 1
print(next(counter2))  # Output: 2
# print(next(counter2))  # Raises StopIteration exception because it's exhausted
#return vs yield:
#• return terminates the function entirely and sends back a single value.
#• yield produces a value, pauses the function's execution, and saves all internal states (variable values, loop position) so it can resume exactly where it left off.

#Recursive Functions: A recursive function is a function that calls itself in order to solve a problem. It typically has a base case to terminate the recursion and prevent infinite loops.
def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case
    print(factorial.__doc__) #Return the factorial of a non-negative integer..


#Anonymous Functions (Lambda Functions): Lambda functions are small, anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have a single expression.
square = lambda x: x ** 2
print(square(5))  # 25

#common built-in functions that can be used with lambda functions include map(), filter(), and reduce().
#!. map() applies a function to all items in an input list.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]

#2. filter() creates a new list containing only the items that satisfy a given condition.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  
print(even_numbers)  # [2, 4]

#3. sorted() returns a new sorted list from the items in an iterable.
sorted_numbers = sorted(numbers, key=lambda x: x)   
print(sorted_numbers)  # [1, 2, 3, 4, 5]
    