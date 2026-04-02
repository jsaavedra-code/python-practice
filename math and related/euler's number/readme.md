# Euler’s Number (e) Approximation Calculator

A simple Python program that approximates **Euler’s number (e)** using its series expansion.

---

## 📌 About

This project calculates an approximation of **e** using the formula:

[
e = \sum_{k=0}^{n} \frac{1}{k!}
]

Instead of recalculating factorials every time, the program uses an **incremental factorial approach**, making it more efficient and clean.

---

## 🚀 Features

* Approximates Euler’s number using **n terms**
* Uses **efficient factorial accumulation**
* Handles invalid input using `try/except`
* Prevents negative inputs
* Displays:

  * Approximation
  * Actual value (`math.e`)
  * Absolute error
* Output formatted to **10 decimal places**

---

## 🧠 How It Works

* Starts with `fact = 1` (which represents `0!`)
* Iteratively builds factorial:

  ```
  k! = (k-1)! × k
  ```
* Adds each term:

  ```
  1 / k!
  ```
* Accumulates the result in `approx`

This avoids recomputing factorials from scratch and improves performance.

---

## ▶️ Usage

Run the program:

```
python your_file_name.py
```

Enter a non-negative integer when prompted:

```
Enter the number of terms to approximate Euler's number (e):
```

---

## 📊 Example Output

```
Approximation of Euler's number (e) using 10 terms: 2.7182818011
Actual value of Euler's number (e): 2.7182818285
Absolute error: 0.0000000274
```

---

## ⚠️ Notes

* Increasing `n` improves accuracy, but factorial grows very fast.
* Around **10–15 terms** already gives high precision.
* Extremely large values of `n` are unnecessary.

---

## 🎯 Purpose

This project demonstrates:

* Loop control (`for`, `while`)
* Input validation (`try/except`)
* Mathematical series implementation
* Basic algorithm optimization

---

## 🧩 Future Improvements

* Stop automatically based on desired precision instead of fixed `n`
* Add performance comparison between naive and optimized factorial
* Turn into a small CLI tool

---

## 👨‍💻 Author

John Saavedra  
GitHub: https://github.com/jsaavedra-code

---

## 🗿 Fun Note

Yes, you *could* just use `math.e`.

But that’s not the point.
