# Simple Bank Account Program
# This program allows the user to deposit, withdraw, and check their balance.
# It runs continuously until the user chooses to exit.

balance = 0

print("Welcome to your personal bank account.")
print("You can deposit, withdraw, and check your balance at any time.")

# Deposit function
def deposit(balance):
    try:
        amount = float(input("Enter the amount you want to deposit: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return balance

    if amount <= 0:
        print("Please enter a positive amount.")
        return balance

    balance += amount
    print(f"Deposit successful. New balance: {balance} $")
    return balance


# Withdraw function
def withdraw(balance):
    try:
        amount = float(input("Enter the amount you want to withdraw: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return balance

    if amount <= 0:
        print("Please enter a positive amount.")
        return balance

    if amount > balance:
        print("Insufficient funds.")
        return balance

    balance -= amount
    print(f"Withdrawal successful. New balance: {balance} $")
    return balance


# Check balance function
def check_balance(balance):
    print(f"Your current balance is: {balance} $")
    return balance


# Main loop
while True:
    print("\nPlease choose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if option == 1:
        balance = deposit(balance)

    elif option == 2:
        balance = withdraw(balance)

    elif option == 3:
        balance = check_balance(balance)

    elif option == 4:
        print("Thank you for using the bank account system. Goodbye.")
        break

    else:
        print("Invalid option. Please select a number between 1 and 4.")