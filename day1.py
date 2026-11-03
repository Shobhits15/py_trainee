#Day 1: Python setup, virtual environments(poetry), variables, core types, operators, input/output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
subject1 = input("Enter the first subject: ")
while True:
    Marks1 = float(input(f"Enter your marks of {subject1}: "))
    if 0 <= Marks1 <= 100:
        break
    print("Invalid marks! Enter a value between 0 and 100.")

subject2 = input("Enter the second subject: ")
while True:
    Marks2 = float(input(f"Enter your marks of {subject2}: "))
    if 0 <= Marks2 <= 100:
        break
    print("Invalid marks! Enter a value between 0 and 100.")

subject3 = input("Enter the third subject: ")
while True:
    Marks3 = float(input(f"Enter your marks of {subject3}: "))
    if 0 <= Marks3 <= 100:
        break
    print("Invalid marks! Enter a value between 0 and 100.")
totalmarks = Marks1 + Marks2 + Marks3
avgmarks = totalmarks / 3
if avgmarks >= 90:
    grade = "A"
elif avgmarks >= 60:
    grade = "B"
else:
    grade = "C"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} cm")
print(f"Subject 1: {subject1}")
print(f"Marks 1: {Marks1}")
print(f"Subject 2: {subject2}")
print(f"Marks 2: {Marks2}")
print(f"Subject 3: {subject3}")
print(f"Marks 3: {Marks3}")
print(f"Total Marks: {totalmarks}")
print(f"Average Marks: {avgmarks}")
print(f"Grade: {grade}")