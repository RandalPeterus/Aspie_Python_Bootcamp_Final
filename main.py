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
    all_transactions = expenses + income
    for transaction in all_transactions:
        print(transaction)

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



    main()