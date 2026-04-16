# ==========================================
# Student Records Manager
# ==========================================
# This program allows the user to:
# - Add students
# - Add grades
# - Check if a student is enrolled in a course
# - Calculate average grades
# - List students by course
# - Filter top students
# - Show all student records
#
# Data is stored in a dictionary:
# key   -> student name
# value -> another dictionary with age, grades, and courses
# ==========================================

student_records = {} # main dictionary to store all student data

# Add a new student to the dictionary
def add_student(name, age, courses):

    if name in student_records:
        print(f"Student '{name}' already exists.")
        return

    student_records[name] = {
        "age": age,
        "grades": set(),          # set() avoids duplicate grades
        "courses": set(courses)   # set() avoids duplicate courses too
    }

    print(f"Student '{name}' added successfully.")


# Add a grade to an existing student
def add_grade(name, grade):

    if name not in student_records:
        print(f"Student '{name}' not found.")
        return 

    student_records[name]["grades"].add(grade)

    print(f"Grade {grade} added for student '{name}'.")


# Check whether a student is enrolled in a course
def is_enrolled(name, course):

    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False

    return course in student_records[name]["courses"]  # returns True or False


# Calculate the average grade of one student
def calculate_average_grade(name):

    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None

    grades = student_records[name]["grades"]

    if not grades:   # if the set is empty
        return 0

    return sum(grades) / len(grades)   # average = total / amount


# Return a list of students enrolled in a specific course
def list_students_by_course(course):

    students = []

    for student in student_records:
        if course in student_records[student]["courses"]:
            students.append(student)

    return students


# Return students whose average grade is above a threshold
def filter_top_students(threshold):

    top_students = []

    for student in student_records:
        grades = student_records[student]["grades"]

        if grades:   # only check students who actually have grades
            avg = calculate_average_grade(student)

            if avg > threshold:
                top_students.append(student)

    return top_students


# Display the menu
def show_menu():
    print()
    print("--- Student Records Menu ---")
    print("1. Add student")
    print("2. Add grade")
    print("3. Check enrollment")
    print("4. Calculate average grade")
    print("5. List students by course")
    print("6. Filter top students")
    print("7. Show all student records")
    print("0. Exit")


# Main program loop
while True:

    show_menu()
    choice = input("Enter your choice: ")

    # --------------------------------------
    # Option 1: Add student
    # --------------------------------------
    if choice == "1":

        name_input = input("Enter student name: ").strip()  # strip removes extra spaces

        # Validate age so the program does not crash if user types letters
        try:
            age_input = int(input("Enter student age: "))
        except ValueError:
            print("Invalid age. Please enter a whole number.")
            continue   # go back to the menu instead of crashing

        courses_input = input("Enter courses (comma-separated): ")
        courses_list = courses_input.split(",")   # split turns one string into a list

        clean_courses = []

        for course in courses_list:
            clean_course = course.strip()   # removes spaces before/after each course
            if clean_course != "":          # avoids adding empty course names
                clean_courses.append(clean_course)

        if name_input == "":
            print("Student name cannot be empty.")
            continue

        add_student(name_input, age_input, clean_courses)

    # --------------------------------------
    # Option 2: Add grade
    # --------------------------------------
    elif choice == "2":

        name_input = input("Enter student name: ").strip()

        try:
            grade_input = float(input("Enter grade to add: "))  # float allows decimals too
        except ValueError:
            print("Invalid grade. Please enter a number.")
            continue

        add_grade(name_input, grade_input)

    # --------------------------------------
    # Option 3: Check enrollment
    # --------------------------------------
    elif choice == "3":

        name_input = input("Enter student name: ").strip()
        course_input = input("Enter course name: ").strip()

        enrolled = is_enrolled(name_input, course_input)

        if name_input in student_records:
            if enrolled:
                print(f"Student '{name_input}' is enrolled in '{course_input}'.")
            else:
                print(f"Student '{name_input}' is NOT enrolled in '{course_input}'.")

    # --------------------------------------
    # Option 4: Calculate average grade
    # --------------------------------------
    elif choice == "4":

        name_input = input("Enter student name: ").strip()
        average = calculate_average_grade(name_input)

        if average is not None:
            print(f"Average grade for '{name_input}' is: {average:.2f}")  # 2 decimal places

    # --------------------------------------
    # Option 5: List students by course
    # --------------------------------------
    elif choice == "5":

        course_input = input("Enter course name: ").strip()
        students_in_course = list_students_by_course(course_input)

        if students_in_course:
            print(f"Students enrolled in '{course_input}':")
            for student in students_in_course:
                print(student)
        else:
            print(f"No students are enrolled in '{course_input}'.")

    # --------------------------------------
    # Option 6: Filter top students
    # --------------------------------------
    elif choice == "6":

        try:
            threshold_input = float(input("Enter grade threshold: "))
        except ValueError:
            print("Invalid threshold. Please enter a number.")
            continue

        top_students = filter_top_students(threshold_input)

        if top_students:
            print(f"Students with average grade above {threshold_input}:")
            for student in top_students:
                print(student)
        else:
            print(f"No students have an average grade above {threshold_input}.")

    # --------------------------------------
    # Option 7: Show all student records
    # --------------------------------------
    elif choice == "7":

        if student_records:
            print()
            print("--- All Student Records ---")

            for student in student_records:
                print(f"Name: {student}")
                print(f"Age: {student_records[student]['age']}")
                print(f"Courses: {student_records[student]['courses']}")
                print(f"Grades: {student_records[student]['grades']}")
                print()
        else:
            print("No student records found.")

    # --------------------------------------
    # Option 0: Exit
    # --------------------------------------
    elif choice == "0":
        print("Exiting the program, bye.")
        break

    # --------------------------------------
    # Invalid choice
    # --------------------------------------
    else:
        print("Invalid choice. Please try again.")