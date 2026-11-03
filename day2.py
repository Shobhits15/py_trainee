#Day 2: Conditions, loops, strings, lists, tuples, sets, dictionaries, slicing and comprehensions.
#Conditions(if, elif, else))
from unicodedata import name


age = int(input("Enter your age: "))
if age >= 18:
    print("Adult.")
elif age >= 13:
    print("Teenager.")
else:
    print("Child.")

#Loops(for, while)
#For loop
for i in range(5):
    print(i)

#While loop
count = 0
while count < 5:
    print(count)
    count += 1

#Break and continue
for n in range(5):
    if n == 2:
        continue
    if n == 4:
        break
    print(n)

#Strings
str = "Shobhit "
print(str)
print(str.upper())       # SHOBHIT
print(str.lower())       # shobhit
print(str.strip())       # Removes surrounding spaces
print(str.replace("S", "s"))
print(len(str))          # 7
print("hob" in str)      # True

#Lists- A list is an ordered, mutable collection.
marks = [90, 80, 70, 50, 40]
print(marks)
print(marks[0])          # 90
print(marks[-1])         # 50
marks.append(95)       # Add an item
marks[0] = 88          # Update an item
marks.remove(70)       # Remove an item
marks.sort()            # Sort the list
print(marks)

#Tuples- A tuple is an ordered, immutable collection.
student = ("Shobhit", 20, 5.9)
print(student[0]) #Shobhit

#Sets- A set is an unordered collection of unique items.
language = {"Python", "Java", "C++", "Python"}
print(language) # {'C++', 'Python', 'Java'} 


a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}

#Dictionaries- A dictionary is an unordered collection of key-value pairs. mutable
student = {"name": "Shobhit", "age": 20, "height": 5.9}
print(student["name"])  # Shobhit
print(student["age"])   # 20
print(student["height"]) # 5.9

student["age"] = 21  # Update value
student["weight"] = 60  # Add new key-value pair
print(student)
print(student.keys()) #dict_keys(['name', 'age', 'height', 'weight'])
print(student.values()) #dict_values(['Shobhit', 21, 5.9, 60])
print(student.items())  #dict_items([('name', 'Shobhit'), ('age', 21), ('height', 5.9), ('weight', 60)])
print(student.get("city", "Not provided"))# Default value if key not found

#Slicing- Extracting parts of a list, string, or tuple.
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # [2, 3, 4]
print(numbers[:3])   # [1, 2, 3]
print(numbers[2:5])  # [3, 4, 5]  
print(numbers[::2])  # [1, 3, 5]  Every second element
print(numbers[::-1]) # [5, 4, 3, 2, 1]  Reversed copy
print(numbers[-2:])   # Last two elements

#Comprehensions- A easy way to create lists, sets, or dictionaries.

#traditional way
numbers = [1, 2, 3, 4, 5]
square= []
for x in numbers:
    square.append(x**2)
print(square)

#List comprehension
square = [x**2 for x in numbers]
print(square) # [1, 4, 9, 16, 25]

#Condition Comprehension
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6]


