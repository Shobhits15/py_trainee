# Week 1: Python Fundamentals

This folder contains hands-on Python lessons from Day 1 through Day 5, along with
small projects that apply the concepts. The examples progress from basic input
and data types to reusable functions, file handling, and object-oriented
programming.

## What I learned

### Day 1 - Python basics and a marks report

- Python setup and virtual environments with Poetry.
- Variables, core data types, type conversion, operators, and console input/output.
- Input validation with loops and conditional logic with `if` / `elif` / `else`.
- **Project:** enter a student's name, age, height, and three subject marks; the
  script validates marks, calculates the total and average, and assigns a grade.

Run with `python day1.py`.

### Day 2 - Collections, conditions, and loops

- Conditional statements and `for` / `while` loops, including `break` and
  `continue`.
- String operations and the list, tuple, set, and dictionary data structures.
- Indexing, slicing, set operations, and list comprehensions.
- **Project:** `day2calc.py` provides reusable average and grade functions,
  including validation for empty lists and marks outside the 0-100 range.
  `tests/day2calc_test.py` checks the calculator behavior and grade boundaries.

Run the lesson with `python day2.py`.

### Day 3 - Functions and reusable code

- Parameters and arguments, positional/keyword/default arguments, and
  variable-length arguments.
- Return values, scope, type hints, docstrings, and imports/modules.
- Generators with `yield`, recursion, lambda functions, `map`, `filter`, and
  sorting with a key function.

Run with `python day3.py`.

### Day 4 - Files and error handling

- Reading, writing, and appending files; working with paths using `pathlib`.
- Context managers (`with`) for reliable resource cleanup.
- Exceptions with `try`, `except`, `else`, and `finally`, plus `assert` and
  `raise`.
- Reading and writing text, CSV, and JSON data with standard-library modules.
- **Examples/data:** student records are in `student.txt`, `student.json`, and
  `students.csv`; additional sample files are under `data/`.

Run with `python day4.py`.

### Day 5 - Classes, OOP, and an expense tracker

- Classes, objects, constructors, instance/class attributes, and instance,
  class, and static methods.
- Dataclasses and composition.
- Encapsulation, inheritance, polymorphism, and abstraction.
- An abstract `PaymentProcessor` contract with credit-card and PayPal
  implementations.
- **Project:** `day5_utility.py` is a command-line expense tracker. It can add,
  list, delete, and filter expenses by category, and calculate totals. It uses
  an `Expense` dataclass and persists records as JSON in `data/expenses.json`.

Run the lesson with `python day5.py`, or start the expense tracker from this
folder with `python day5_utility.py`.

## Project layout

```text
day1.py                 Student marks and grade report
day2.py                 Conditions, loops, strings, and collections lesson
day2calc.py             Reusable marks calculator functions
day3.py                 Functions and modules lesson
day4.py                 File handling and exceptions lesson
day5.py                 OOP concepts and payment processor examples
day5_utility.py         JSON-backed command-line expense tracker
data/                   Expense and student sample data
tests/day2calc_test.py  Calculator unit tests
tests/day5.py           Student class example
pyproject.toml           Poetry project and dependency configuration
```

## Run the tests

Install the project dependencies with Poetry, then run:

```powershell
poetry install
poetry run python -m pytest
```

The project configuration requires Python 3.14 or newer.