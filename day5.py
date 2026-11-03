#Day 5 Classes/objects, dataclasses and composition: choose oop only when it improves clarity; build a file based utility


#1.Class-A blueprint for creating objects
class Dog:
    sound = "Bark"

#2 Object- the reality or an actual entity created based on the class blueprint
#stored in memory and has a unique identity
dog1 = Dog()
print(dog1.sound)  # Output: Bark

#Dataclass- A decorator that automatically generates special methods like __init__(), __repr__(), and __eq__().
#reducing boilerplate code.
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0  # Default value

# Usage
item = Product(name="Laptop", price=999.99, quantity=2)

print(item)        # Output: Product(name='Laptop', price=999.99, quantity=2)
print(item.price)  # Output: 999.99


#Composition (Has a relation)

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")


car = Car()
car.drive()

#OOPs
#1. Encapsulation- The bundling of data and methods and controlloing access to the internal state of an object.

class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

emp = Employee("Fedrick", 50000)
print(emp.name)       #Fedrick
print(emp.__salary)  #Error

#Access Specifiers- how class members can be accessed from outside the class
#  Public- accessible from anywhere
class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible

#  Protected- accessible within the class and its subclasses
#denoted by a single underscore (_)

class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass

#  Private- accessible only within the class
#denoted by double underscore (__)
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def display_salary(self):
        print("Salary:", self.__salary)  # Accessible within the class

#2. Abstraction- The process of hiding the implementation details and showing only the essential features of an object.  
#@abstractmethod decorator, allowing developers to enforce method implementation in subclasses while hiding complex internal logic.
from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())

#3. Inheritance- The mechanism by which one class can inherit properties of another class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy barks
print(cat.speak())  # Output: Whiskers meows

#Types of Inheritance:
#1. Single Inheritance- A class inherits from a single parent class.
class Vehicle:
    def move(self):
        return "Moving forward"

class Car(Vehicle):  # Car inherits from Vehicle
    def honk(self):
        return "Beep Beep!"

my_car = Car()
print(my_car.move())  # Output: Moving forward

#2. Multiple Inheritance- A class can inherit from multiple parent classes.
class Flyable:
    def fly(self):
        return "Flying in the sky"

class Swimmable:
    def swim(self):
        return "Swimming in water"


class Duck(Flyable, Swimmable):  # Duck inherits from both Flyable and Swimmable
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())   # Output: Flying in the sky
print(duck.swim())  # Output: Swimming in water
print(duck.quack()) # Output: Quack!

#3. Multilevel Inheritance- A class inherits from a parent class, which in turn inherits from another parent class.
class Animal:
    def eat(self):
        return "Eating food"

class Mammal(Animal):  # Inherits eat()
    def walk(self):
        return "Walking"

class Dog(Mammal):     # Inherits eat() and walk()
    def bark(self):
        return "Woof!"

husky = Dog()
print(husky.eat())   # Output: Eating food
print(husky.bark())  # Output: Woof!

#4. Hierarchical Inheritance- Multiple classes inherit from a single parent class.
class Shape:
    def info(self):
        return "I am a geometric shape"

class Circle(Shape):  # Inherits info()
    pass

class Square(Shape):  # Inherits info()
    pass

#5. Hybrid Inheritance- A combination of two or more types of inheritance.
class Base:
    pass

class SubA(Base):
    pass

class SubB(Base):
    pass

class HybridChild(SubA, SubB):  # Combines Hierarchical and Multiple models
    pass

#4. Polymorphism- same function to behave differently based on the object that is calling it.

#types 
#Compile-time polymorphism allows multiple methods with the same name but different parameters, with the appropriate method selected before execution.
#Method Ovverloading

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

calc = Calculator()
print(calc.multiply())            
print(calc.multiply(4))  
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))

#Runtime polymorphism means that the behavior of a method is decided while program is running, based on the object calling it.
#Method Overriding

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())