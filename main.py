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
categories = []
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
    total_expenses = sum(expense["Expense"] for expense in expenses)
    total_income = sum(inc["Income"] for inc in income)
    net_balance = total_income - total_expenses

    print("Total expenses:")
    print(f"${total_expenses:.2f}")
    print("Total income:")
    print(f"${total_income:.2f}")
    print("Net balance:")
    print(f"${net_balance:.2f}")


"""
Allows the user to create a category for their transactions. 
This function will prompt the user for a category name and store it in a list of categories.
"""

def create_category():

    while True:
        category_name = input("Enter a name for the new category (or 'q' to cancel): ").strip()
        if category_name.lower() == 'q':
            break
        if category_name:
            categories.append(category_name)
            print(f"Category '{category_name}' created.")
        else:
            print("Please enter a valid category name.")

def assign_category():
    if not expenses and not income:
        print("There are no transactions to assign categories to.")
        return

    if not categories:
        print("No categories available. Please create a category first.")
        return

    all_transactions = expenses + income
    for i, transaction in enumerate(all_transactions):
        print(f"{i + 1}: {transaction}")

    index = input("Enter the number of the transaction to assign a category (or 'q' to cancel): ").strip().lower()
    if index == "q":
        return

    try:
        index = int(index) - 1
        if not 0 <= index < len(all_transactions):
            print("Invalid transaction index. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print("Available categories:")
    for j, category in enumerate(categories):
        print(f"{j + 1}: {category}")

    category_index = input("Enter the number of the category to assign: ").strip().lower()
    try:
        category_index = int(category_index) - 1
        if not 0 <= category_index < len(categories):
            print("Invalid category index. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    all_transactions[index]["Category"] = categories[category_index]
    print(f"Assigned category '{categories[category_index]}' to transaction: {all_transactions[index]}")

"""

Calculates the total expenses and income for each category and displays the results.

"""

def category_summary():
    if not categories:
        print("No categories available.")
        return

    category_totals = {category: 0.0 for category in categories}

    for transaction in expenses + income:
        if "Category" in transaction:
            category = transaction["Category"]
            if "Expense" in transaction:
                category_totals[category] -= transaction["Expense"]
            elif "Income" in transaction:
                category_totals[category] += transaction["Income"]

    print("Category Summary:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

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
        print("7: Create a category")
        print("8: Assign a category to a transaction")
        print("9: View category summary")
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
        elif choice == "7":
            create_category()
        elif choice == "8":
            assign_category()
        elif choice == "9":
            category_summary()
        elif choice == "q":
            print("Good Evening.")
        else:
            print("Sorry, that's not a valid option. Please try again.")


if __name__ == "__main__":
    main()