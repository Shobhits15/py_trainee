#File Based utility 
# its an Expense Tracker that saves expenses in a JSON file, so records remain available after the program closes.

from dataclasses import dataclass, asdict
from pathlib import Path
import json
from datetime import date
from turtle import title



#DataClass
@dataclass
class Expense:
    title: str
    amount: float
    category: str
    expense_date: str

class ExpenseStore:

    def __init__(self, file_path: Path):
        self.file_path = file_path

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def load(self) -> list[Expense]:

        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open(
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)  #Reads JSON

            if not isinstance(data, list):
                raise ValueError("Invalid expense file structure")

            return [Expense(**item) for item in data] #Expense(**item) creates an Expense object from a dictionary

        except json.JSONDecodeError as error:
            raise ValueError("Expense file contains invalid JSON") from error

    def save(self, expenses: list[Expense]):

        data = [asdict(expense) for expense in expenses] #asdict() - converts a dataclass object into a dictionary

        with self.file_path.open(   #with - Context manager
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(data, file, indent=4) #Writes JSON
#In class ExpenseStore:

class ExpenseTracker:


    def __init__(self, store: ExpenseStore):
        self.store = store

    def add_expense(self, title, amount, category):

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        expenses = self.store.load()

        expense = Expense(
            title=title,
            amount=amount,
            category=category,
            expense_date=date.today().isoformat()
        )

        expenses.append(expense)

        self.store.save(expenses)

        print("Expense added successfully!")

    def show_expenses(self):

        expenses = self.store.load()

        if not expenses:
            print("No expenses found.")
            return

        for expense in expenses:
            print(
                f"{expense.title} | "
                f"₹{expense.amount:.2f} | "
                f"{expense.category} | "
                f"{expense.expense_date}"
            )

    def show_total(self):

        expenses = self.store.load()

        total = sum(expense.amount for expense in expenses)

        print(f"Total expenses: ₹{total:.2f}")

    def delete_expense(self, title):

        expenses = self.store.load()

        for expense in expenses:
            if expense.title.lower() == title.lower():
                expenses.remove(expense)
                self.store.save(expenses)
                print(f"'{title}' deleted successfully!")
                return

        print("Expense not found.")


    def show_by_category(self, category):

        expenses = self.store.load()

        filtered_expenses = [
            expense
            for expense in expenses
            if expense.category.lower() == category.lower()
        ]

        if not filtered_expenses:
            print(f"No expenses found in category: {category}")
            return

        print(f"\nExpenses in category: {category}")

        for expense in filtered_expenses:
            print(
                f"{expense.title} | "
                f"₹{expense.amount:.2f} | "
                f"{expense.category} | "
                f"{expense.expense_date}"
            )

        total = sum(expense.amount for expense in filtered_expenses)

        print(f"Category Total: ₹{total:.2f}")
#This is composition through dependency injection:
#we pass the store object into the tracker instead of making the tracker responsible for creating and managing the file-storage implementation.

#Main Function:the application entry point
def main():

    store = ExpenseStore(Path("data/expenses.json"))
    tracker = ExpenseTracker(store)

    while True:

        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total")
        print("4. Delete Expense")
        print("5. View Expenses by Category")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                title = input("Enter title: ")
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")

                tracker.add_expense(title, amount, category)

            elif choice == "2":
                tracker.show_expenses()

            elif choice == "3":
                tracker.show_total()

            elif choice == "4":

                title = input("Enter expense title to delete: ")

                tracker.delete_expense(title)

            elif choice == "5":

                category = input("Enter category: ")

                tracker.show_by_category(category)

            elif choice == "6":

                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except (ValueError, OSError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()

    