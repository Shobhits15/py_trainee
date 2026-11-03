#Day 4: File operations with pathlib; safely read/write text, CSV and JSON; exceptions and context managers.

#1. The most common operations are:
#Operation	Python	Purpose
#Read	open()	Read file content
#Write	open()	Create or overwrite a file
#Append	open()	Add content to an existing file
#Delete	Path.unlink()	Delete a file
#Check existence	Path.exists()	Check whether a file exists

#Mode	Meaning
#"r"	Read a file
#"w"	Write; overwrites existing content
#"a"	Append content
#"x"	Create a new file; fails if it exists
#"rb"	Read binary data
#"wb"	Write binary data

#writing to a file
file = open("student.txt", "w", encoding="utf-8")

file.write("Name: Shobhit\n")
file.write("Course: Python\n")

file.close()


#reading from a file
file = open("student.txt", "r", encoding="utf-8")

content = file.read()

print(content)

file.read()        # Reads entire file
file.readline()    # Reads one line
file.readlines()   # Returns all lines as a list

file.close()


#2. pathlib
#pathlib is a Python module used to work with file paths and directories.
#Instead of manually joining paths using strings, it provides the Path class.

from pathlib import Path #Path class is used to represent file paths and directories in a platform-independent way.

file_path = Path("student.txt")

print(file_path) 
print(file_path.name) # student.txt   file name with extension
print(file_path.suffix) # .txt file extension
print(file_path.stem) # student   file name without extension

from pathlib import Path

folder = Path("data")

folder.mkdir(exist_ok=True)


if file_path.exists(): # Check if the file exists
    print("File exists")
else:
    print("File does not exist")

#3. Context managers: Context managers are used to manage resources, such as files, ensuring that they are properly acquired and released. The most common use case is with the with statement, which automatically handles opening and closing files.

#When working with files, we need to close them after completing operations.

#If we forget to close a file, it can cause resource-management problems.
#Problem: If an exception occurs before file.close(), the file might remain open.
#But with context managers, the file is automatically closed when the block is exited, even if an exception occurs.

with open("student.txt", "r", encoding="utf-8") as file: #utf-8 is a character encoding that can represent any character in the Unicode standard. It is widely used for text files and web content.
    content = file.read()
    print(content)



#Exceptions:An exception is an error that occurs while a program is executing.
#Python uses try, except, else, and finally blocks to handle exceptions.

#try:
    # Code that might cause an exception

#except ExceptionType:
    # Handle the exception

#else:
    # Runs if no exception occurs

#finally:
    # Runs whether an exception occurs or not

def process_age(age_input):
    try:
        print("\n--- Starting try block ---") 
        
        # 1. Using 'assert' to debug assumptions (must be a number)
        # If False, it automatically raises an AssertionError
        assert isinstance(age_input, (int, float)), "Age input must be numeric!"    #assert - checks a condition and raises an AssertionError if the condition is False.

        # 2. Using 'raise' to deliberately enforce business logic rules
        if age_input < 0:
            raise ValueError("Age cannot be negative.")  #raise - manually raises an exception
        
        # This line only executes if assert and raise don't trigger
        print(f"Success! Age is valid: {age_input}")

    except AssertionError as error:
        # Catches the failed assert statement
        print(f"Caught an AssertionError: {error}")

    except ValueError as error:
        # Catches the manually raised negative check
        print(f"Caught a ValueError: {error}")

    except Exception as error:
        # Fallback catch-all for any other unexpected errors
        print(f"Caught a generic error: {error}")

    else:
        # Runs ONLY if the try block succeeds with no errors
        print("Else block executed: Processing completed without errors.")

    finally:
        # ALWAYS runs, no matter what happens above
        print("Finally block executed: Cleanup actions completed.")

# =====================================================================
# Testing all possible scenarios to see how the blocks behave
# =====================================================================

print("Scenario 1: Passing a valid age")
process_age(25)

print("\nScenario 2: Triggering the 'raise' keyword")
process_age(-5)

print("\nScenario 3: Triggering the 'assert' keyword")
process_age("twenty-five")


#Safely Reading and Writing Text Files-combine pathlib, context managers, and exceptions.
#Writing text
from pathlib import Path

file_path = Path("data/student.txt")

file_path.parent.mkdir(parents=True, exist_ok=True)

try:
    file_path.write_text(
        "Name: Shobhit\nCourse: Python",
        encoding="utf-8"
    )

    print("File written successfully")

except OSError as error:
    print("File operation failed:", error)

#Reading text

from pathlib import Path

file_path = Path("data/student.txt")

try:
    with file_path.open("r", encoding="utf-8") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("Student file not found")

except OSError as error:
    print("Unable to read file:", error)

#Writing and reading CSV files
#CSV (Comma-Separated Values) files are a common format for storing tabular data. Python provides the csv module to read and write CSV files.
#Writing CSV files
import csv
from pathlib import Path

file_path = Path("students.csv")

students = [
    {"name": "Shobhit", "age": 22, "marks": 90},
    {"name": "Rahul", "age": 22, "marks": 85},
    {"name": "Aman", "age": 24, "marks": 95}
]

with file_path.open("w", newline="", encoding="utf-8") as file:

    fieldnames = ["name", "age", "marks"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students) 



#Reading CSV files
import csv
from pathlib import Path

file_path = Path("students.csv")

try:
    with file_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("CSV file not found")



#Writing and reading JSON files
#JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy
#Writing JSON files
import json
from pathlib import Path

student = {
    "name": "Shobhit",
    "age": 22,
    "course": "Python"
}

file_path = Path("student.json")

with file_path.open("w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

#Reading JSON files
import json
from pathlib import Path

file_path = Path("student.json")

try:
    with file_path.open("r", encoding="utf-8") as file:
        student = json.load(file)

    print(student["name"])
    print(student["course"])

except FileNotFoundError:
    print("JSON file not found")

except json.JSONDecodeError:
    print("Invalid JSON format")

except OSError as error:
    print("File operation failed:", error)

#Method             	Purpose
#json.dump()	Writes JSON directly to a file
#json.dumps()	Converts Python data into a JSON string
#json.load()	Reads JSON from a file
#json.loads()	Converts a JSON string into Python data
