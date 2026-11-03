#Day5:Day 5 Classes/objects, dataclasses and composition: choose oop only when it improves clarity; build a file based utility

#1.Class- A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
#2. Object- An instance of a class. It represents a specific entity that has the attributes and methods defined by the class.

class Student:  #class

    def display(self): #function/method
        print("Student details")


student1 = Student() #object1
student2 = Student() #object2

student1.display()
student2.display()

#3.Constructor- A special method in a class that is automatically called when an object of the class is created.
#  It is used to initialize the attributes of the object. 
# _init_() is used to define the constructor in Python.

class Student:

    def __init__(self, name, age, marks): #constructor
        self.name = name  #self refers to the current instance of the class and is used to access the attributes and methods of the class.
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


student1 = Student("Shobhit", 23, 90)  #object

student1.display()