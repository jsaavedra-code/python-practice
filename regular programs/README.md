# Daily Expense Tracker

A simple Python program to track daily expenses from the terminal.

---

## What it does

This program lets the user:

* add a new expense
* view all recorded expenses
* calculate total and average expense
* clear all expenses
* exit the program

It runs in a loop and works through a simple numeric menu.

---

## Features

* stores expenses in a list
* supports decimal values using `float`
* numbers expenses automatically when displaying them
* handles empty-list cases
* calculates:

  * total expense
  * average expense
* clears all saved expenses in one step

---

## How it works

The program starts by showing a menu with 5 options:

1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit

The user enters a number, and the program reacts accordingly.

---

## Example flow

```text
Welcome to my Daily Expense Tracker

Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit
```

Example interaction:

```text
1
23.5
Expense added successfully.

1
12
Expense added successfully.

2
These are your expenses:
1. 23.5
2. 12.0

3
Total expense: 35.5
Average expense: 17.75
```

---

## Concepts used

This project uses:

* `while True`
* `if / elif / else`
* lists
* `append()`
* `enumerate()`
* loops
* basic arithmetic
* simple state management

---

## Why this exists

Because not everything has to be:

* a joke project
* a toy script
* or a massive app with 14 files and emotional damage

Sometimes a small terminal program is enough to show:

* logic
* structure
* usefulness
* and whether someone can build something that actually works

---

## Notes

This is a simple version and can still be improved.

Possible future upgrades:

* input validation with `try/except`
* save expenses to a file
* categories for expenses
* date tracking
* better formatting for currency

---

## Author

John Saavedra
GitHub: https://github.com/jsaavedra-code

---

## Final note

This is a regular program, not a meme project.

Still, I would rather write something functional with personality than make another lifeless “enterprise-grade” calculator pretending to have a soul.
