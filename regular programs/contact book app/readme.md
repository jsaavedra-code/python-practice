# 📒 Contact Book

## 🧠 Overview

A simple Python-based contact management app that allows users to store and manage contacts through a menu-driven interface.

This project focuses on practicing dictionaries, functions, and basic program flow.

---

## ⚙️ Features

* ➕ Add a new contact
* 🔍 View a contact’s details
* ✏️ Edit existing contact information
* ❌ Delete a contact
* 📋 List all contacts
* 🚪 Exit the application

---

## 🗂️ Data Structure

The contact book is implemented using a dictionary:

```python
contact_book = {
    "Name": {
        "phone": "...",
        "email": "...",
        "address": "..."
    }
}
```

* Keys → contact names
* Values → dictionaries with contact details

---

## 🔁 Core Logic

* Uses functions to separate each operation
* Checks if a contact exists before modifying or deleting
* Updates only fields that are provided (skips empty input)
* Runs in a loop with a menu system

---

## 🧩 Concepts Used

* Dictionaries (nested)
* Functions
* Conditionals (`if / else`)
* User input handling
* Basic CRUD logic

---

## ⚠️ Notes

* Contact names must be unique
* Data is stored in memory only (no file/database)
* Input is not strictly validated

---

## 👤 Author

**John Saavedra**  
GitHub: [https://github.com/jsaavedra-code](https://github.com/jsaavedra-code)
