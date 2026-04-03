# This is a simple daily expense tracker program that allows users to add, view, calculate total and average expenses, and clear all expenses.

expense_list = []
total_expense = 0
average_expense = 0

print("Welcome to my Daily Expense Tracker")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

while True:
    option = int(input())

    if option == 1:
        expense = float(input())
        expense_list.append(expense)
        print("Expense added successfully.")

    elif option == 2:
        if not expense_list:
            print("No expenses recorded yet.")
        else:
            print("These are your expenses:")
            for index, value in enumerate(expense_list, start = 1):
                print(f"{index}. {value}")

    elif option == 3:
        if not expense_list:
            print("No expenses recorded yet.")
        else:
            for i in expense_list:
                total_expense += i
            average_expense = total_expense / len(expense_list)
            print(f"Total expense: {total_expense}")
            print(f"Average expense: {average_expense}")

    elif option == 4:
        expense_list = []
        print("All expenses cleared.")
    
    elif option == 5:
        print("Thanks for using my Daily Expense Tracker, toodles.")
        break

    else:
        print("Please select a valid option.")



        