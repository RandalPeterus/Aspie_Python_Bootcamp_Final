"""
Aspie Bootcamp 
Python Final Project
Personal Finance Manager
Ryan Sfiligoi

Objective:
Create a Python application that acts as a personal finance manager. The program will help users to track their income, expenses, and provide basic financial summaries.
"""

import datetime

expenses = []
income = []
"""
Adding in a function that requests the name, time, and amount for the income or expenses
"""

def add_expense_income(entry_type):
    if entry_type == "expense":
        while True:
            name = input("Enter a name for this expense: ").strip()
            if name:
                break
            print("Please enter a valid name.")

        while True:
            try:
                amount = float(input("Enter the expense amount: ").strip())
                if amount > 0:
                    break
                print("Please enter a valid amount greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

        time = datetime.datetime.now()
        expenses.append({
            "Time": time.strftime("%Y-%m-%d %H:%M"),
            "Name": name,
            "Expense": amount,
        })

    elif entry_type == "income":
        while True:
            name = input("Enter a name for this income: ").strip()
            if name:
                break
            print("Please enter a valid name.")

        while True:
            try:
                amount = float(input("Enter the income amount: ").strip())
                if amount > 0:
                    break
                print("Please enter a valid amount greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

        time = datetime.datetime.now()
        income.append({
            "Time": time.strftime("%Y-%m-%d %H:%M"),
            "Name": name,
            "Income": amount,
        })

"""
Prints everything, nothing complex for this
"""
def print_transactions():
    """
    all_transactions = expenses + income
    for transaction in all_transactions:
        print(transaction)
    """
    if not expenses and not income:
        print("There are no transactions to display.")
        return

    all_transactions = expenses + income

    for transaction in all_transactions:

        time = transaction["Time"]
        name = transaction["Name"]

        if "Expense" in transaction:
            amount = transaction["Expense"]
            transaction_type = "expense"

        else:
            amount = transaction["Income"]
            transaction_type = "income"

        print(
            f"At {time}, the {transaction_type}, "
            f"{name}, was made for ${amount:.2f}."
        )

""" 
Deletes transactions        
"""
def delete_transaction():

    while True:
        print("\nWhat type of transaction would you like to delete?")
        print("1: Expense")
        print("2: Income")
        print("q: Cancel")

        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            if not expenses:
                print("No expenses to delete.")
                return
            print("\nExpenses:")
            for i, expense in enumerate(expenses):
                print(f"{i + 1}: {expense}")
            index = input("Enter the number of the expense to delete (or 'q' to cancel): ").strip().lower()
            if index == "q":
                return
            try:
                index = int(index) - 1
                if 0 <= index < len(expenses):
                    deleted_expense = expenses.pop(index)
                    print(f"Deleted expense: {deleted_expense}")
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            if not income:
                print("No income to delete.")
                return
            print("\nIncome:")
            for i, inc in enumerate(income):
                print(f"{i + 1}: {inc}")
            index = input("Enter the number of the income to delete (or 'q' to cancel): ").strip().lower()
            if index == "q":
                return
            try:
                index = int(index) - 1
                if 0 <= index < len(income):
                    deleted_income = income.pop(index)
                    print(f"Deleted income: {deleted_income}")
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "q":
                return

        else:
                print("Invalid choice. Please try again.")

"""
Modifies transactions
"""

def modify_transaction():
    while True:
        print("\nWhat type of transaction would you like to modify?")
        print("1: Expense")
        print("2: Income")
        print("q: Cancel")

        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            if not expenses:
                print("No expenses to modify.")
                return
            print("\nExpenses:")
            for i, expense in enumerate(expenses):
                print(f"{i + 1}: {expense}")
            index = input("Enter the number of the expense to modify (or 'q' to cancel): ").strip().lower()
            if index == "q":
                return
            try:
                index = int(index) - 1
                if 0 <= index < len(expenses):
                    new_name = input("Enter the new name for this expense: ").strip()
                    new_amount = float(input("Enter the new amount for this expense: ").strip())
                    expenses[index]["Name"] = new_name
                    expenses[index]["Expense"] = new_amount
                    print(f"Modified expense: {expenses[index]}")
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            if not income:
                print("No income to modify.")
                return
            print("\nIncome:")
            for i, inc in enumerate(income):
                print(f"{i + 1}: {inc}")
            index = input("Enter the number of the income to modify (or 'q' to cancel): ").strip().lower()
            if index == "q":
                return
            try:
                index = int(index) - 1
                if 0 <= index < len(income):
                    new_name = input("Enter the new name for this income: ").strip()
                    new_amount = float(input("Enter the new amount for this income: ").strip())
                    income[index]["Name"] = new_name
                    income[index]["Income"] = new_amount
                    print(f"Modified income: {income[index]}")
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "q":
            return

        else:
            print("Invalid choice. Please try again.")
"""
Create a total expenses variable and extract the number 


Self note: Look into how .split works later, need to figure out why -1 worked.

It just gives the last number on the list, so it will pull the number because the number is the last number in each entry.
"""

def calculations():
    total_expenses = 0.0
    for item in expenses:
        amount = item.split()[-1]
        total_expenses += float(amount)

    total_income = 0.0
    for item in income:
        amount = item.split()[-1]
        total_income += float(amount)

    net_balance = total_income - total_expenses

    print("Total expenses:")
    print(f"${total_expenses:.2f}")
    print("Total income:")
    print(f"${total_income:.2f}")
    print("Net balance:")
    print(f"${net_balance:.2f}")

def main():
    print("Good Morning.")
    choice = ""
    while choice != "q":
        print("Finance Tracking App")
        print("What would you like to do?")
        print("1: Add an expense")
        print("2: Add an income")
        print("3: View finance report")
        print("4: View summary statistics")
        print("5: Modify a transaction")
        print("6: Delete a transaction")
        print("q: Quit application")

        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            add_expense_income("expense")
        elif choice == "2":
            add_expense_income("income")
        elif choice == "3":
            print_transactions()
        elif choice == "4":
            calculations()
        elif choice == "5":
            modify_transaction()
        elif choice == "6":
            delete_transaction()
        elif choice == "q":
            print("Good Evening.")
        else:
            print("Sorry, that's not a valid option. Please try again.")


if __name__ == "__main__":
    main()