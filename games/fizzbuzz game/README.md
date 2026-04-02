# 🎮 FizzBuzz Game (Python) — Custom Twist

Welcome to my FizzBuzz project!
This is a modified version of the classic FizzBuzz problem with an additional rule to make it more interesting.

---

## 🚀 Overview

This program:

* Takes a number as input
* Prints the FizzBuzz results from **1 up to that number**
* Applies a custom rule involving the digit **3**

---

## 🧠 Rules

For each number:

* If divisible by **3 and 7** → `"FizzBuzz"`
* If divisible by **7** → `"Buzz"`
* If divisible by **3** → `"Fizz"`
* If the number **contains the digit 3** → `"Almost Fizz"`
* Otherwise → the number itself

---

## 🧩 Core Function

```python
def fizzbuzz(n):
```

This function:

* Receives an integer `n`
* Applies the rules in order
* Returns the corresponding result as a string

---

## ▶️ How to Run

1. Make sure you have Python installed
2. Run the file:

```bash
python fizzbuzz.py
```

3. Enter a number when prompted:

```
Please enter a number:
```

---

## 💡 Example

```
Input: 15

Output:
1
2
Fizz
4
5
Fizz
Buzz
8
Fizz
10
11
Fizz
Almost Fizz
Buzz
Fizz
```

---

## 🛠️ Features

* Function-based logic (reusable and clean)
* Loop iteration from 1 to N
* Custom condition using string conversion (`"3" in str(n)`)
* Clear and beginner-friendly structure

---

## ⚠️ Important Note

The order of conditions matters:

* Divisibility checks are evaluated **before** the `"Almost Fizz"` rule
* This ensures numbers like `3`, `6`, or `21` still return `"Fizz"` or `"FizzBuzz"` instead of `"Almost Fizz"`

---
## 👤 Author

John Saavedra  
GitHub: https://github.com/jsaavedra-code
---

## ⭐ Final Thoughts

A simple project with a creative twist.
Demonstrates:

* Logical thinking
* Condition ordering
* Reusable function design

Small project, but a clean step forward in Python development.
