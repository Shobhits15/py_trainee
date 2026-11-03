#Decorator- A function that takes another function as an argument and extends the behavior of function without changinh the actual code.

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello, World!")
greet()

