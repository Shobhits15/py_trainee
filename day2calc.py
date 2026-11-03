#Day2 pytest part
def calculate_avg(marks):
    if not marks:
        raise ValueError("Marks cannot be empty")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")

    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 60:
        return "B"
    else:
        return "C"