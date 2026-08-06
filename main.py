"""""
Aspie Bootcamp 
Python Final Project
Personal Finance Manager
Ryan Sfiligoi

Objective:
Create a Python application that acts as a personal finance manager. The program will help users to track their income, expenses, and provide basic financial summaries.
"""""
import datetime
expenses = []
income = []
"""""
Adding in a function that requests the name, time, and amount for the income or expenses
"""""
def add_expense_income(entry_type):
    if entry_type == "expense":
        name = input("Enter a name for this expense: ").strip()
        time = datetime.datetime.now()
        amount = input("Enter the expense amount: ").strip()
        expenses.append(f"At {time.strftime("%Y-%m-%d %H:%M")}, {name}, Expense: {amount}")
    elif entry_type == "income":
        name = input("Enter a name for this income: ").strip()
        time = datetime.datetime.now()
        amount = input("Enter the income amount: ").strip()
        income.append(f"At {time.strftime("%Y-%m-%d %H:%M")}, {name}, Income: {amount}")

"""""
Prints everything, nothing complex for this
"""""
def print_transactions():
    all_transactions = expenses + income
    print(all_transactions)
"""""
Create a total expenses variable and extract the number 


Self note: Look into how .split works later, need to figure out why -1 worked.

It just gives the last number on the list, so it will pull the number because the number is the last number in each entry.
"""""
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
    print(f"${total_expenses}")
    print("Total income:")
    print(f"${total_income}")
    print("Net balance:")
    print(f"${net_balance}")

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
        print("q: Quit application")

        choice = input()

        if choice == "1":
            add_expense_income("expense")
        elif choice == "2":
            add_expense_income("income")
        elif choice == "3":
            print_transactions()
        elif choice == "4":
            calculations()
        elif choice == "q":
            print("Good Evening.")
        else:
            print("Sorry, that's not a valid option. Please try again.")


main()