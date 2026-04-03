# Bank Account Program

A simple Python-based bank account system that allows users to deposit, withdraw, and check their balance through a command-line interface.

---

## Overview

This program simulates basic banking operations using a continuous loop. Users can interact with the system by selecting options from a menu.

The application focuses on:

* clean structure
* input validation
* modular design using functions

---

## Features

* Deposit funds into the account
* Withdraw funds with balance validation
* View current account balance
* Prevent invalid inputs (non-numeric values, negative amounts)
* Continuous interaction until user exits

---

## How It Works

When the program starts, it initializes the account balance to 0 and displays a menu with the following options:

1. Deposit
2. Withdraw
3. Check Balance
4. Exit

The user selects an option, and the program performs the corresponding operation using dedicated functions.

---

## Example Usage

```text
Welcome to your personal bank account.

Please choose an option:
1. Deposit
2. Withdraw
3. Check Balance
4. Exit

Enter your choice: 1
Enter the amount you want to deposit: 100

Deposit successful. New balance: 100.0 $
```

---

## Program Structure

The program is divided into three main functions:

* `deposit(balance)`

  * Validates input
  * Adds funds to the balance
  * Returns updated balance

* `withdraw(balance)`

  * Validates input
  * Checks for sufficient funds
  * Deducts amount from balance
  * Returns updated balance

* `check_balance(balance)`

  * Displays the current balance
  * Returns balance (for consistency)

The main loop handles user interaction and calls these functions accordingly.

---

## Concepts Used

* `while True` loop for continuous execution
* `try/except` for error handling
* functions (`def`) for modular design
* conditionals (`if / elif / else`)
* basic arithmetic operations
* user input handling

---

## Possible Improvements

* Store balance in a file (persistent data)
* Add transaction history
* Support multiple users/accounts
* Format currency output more cleanly
* Add authentication (PIN system)

---

## Author

John Saavedra  
Github: https://github.com/jsaavedra-code

---

## Notes

This project demonstrates the transition from basic scripting to structured program design.
It prioritizes clarity, correctness, and maintainability over unnecessary complexity.
