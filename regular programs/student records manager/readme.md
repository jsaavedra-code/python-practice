# 🎓 Student Records System

A simple command-line Python application to manage student records, including enrollment, grades, and performance analysis.

---

## 📌 Description

This project simulates a basic student management system using Python. It allows users to store and manage student data such as courses and grades through a menu-driven interface.

The system is designed as a beginner-friendly project to practice core programming concepts while building something functional.

---

## 🚀 Features

* 📥 Add new students with their courses
* 📝 Add grades to existing students
* ✅ Check if a student is enrolled in a course
* 📊 Calculate average grade per student
* 🔍 List students by course
* 🏆 Filter students above a grade threshold
* 📋 Display all student records

---

## 🧠 Concepts Used

* Dictionaries (nested data structures)
* Sets (to avoid duplicate values)
* Functions
* Loops (`while`, `for`)
* Conditional logic (`if/elif/else`)
* Exception handling (`try/except`)
* User input validation

---

## 🖥️ How to Run

1. Make sure you have Python installed (Python 3 recommended)

2. Clone the repository:

```bash
git clone https://github.com/jsaavedra-code/student-records-system.git
```

3. Navigate to the project folder:

```bash
cd student-records-system
```

4. Run the program:

```bash
python main.py
```

---

## 🛠️ Functions Overview

### `add_student(name, age, courses)`

Adds a new student with their age and list of courses.

### `add_grade(name, grade)`

Adds a grade to an existing student.

### `is_enrolled(name, course)`

Returns `True` or `False` depending on whether the student is enrolled in a specific course.

### `calculate_average_grade(name)`

Returns:

* Average grade (`float`)
* `0` if the student has no grades
* `None` if the student does not exist

### `list_students_by_course(course)`

Returns a list of student names enrolled in a given course.

### `filter_top_students(threshold)`

Returns a list of students whose average grade is above a given threshold.

---

## 📂 Example Usage

```python
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])

add_grade("Alice", 90)
add_grade("Alice", 85)

print(calculate_average_grade("Alice"))  # 87.5
print(list_students_by_course("Math"))   # ['Alice']
```

---

## ⚠️ Notes

* Grades are stored in a `set`, meaning duplicate grades are not allowed.
* Input validation is handled using `try/except` to prevent crashes.
* This is a CLI (Command Line Interface) application — no GUI included.

---

## 🔮 Future Improvements

* Save/load data using JSON files
* Replace `set` with `list` for more realistic grade tracking
* Add a graphical user interface (GUI)
* Implement student IDs instead of names as keys

---

## 👤 Author  
**John Saavedra**    
GitHub: https://github.com/jsaavedra-code  
