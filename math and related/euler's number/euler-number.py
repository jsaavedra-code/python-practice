# Welcome to my Euler's number (e) approximation calculator
# This program calculates the value of Euler's number (e) 

import math

def euler_number_approximation(n):
    approx = 0
    fact = 1  # This will hold the factorial value
    for k in range(n + 1):
        if k > 0:
            fact *= k # Update factorial for the current term
        approx += 1 / fact 
    return approx

while True:
    try: 
        n = int(input("Enter the number of terms to approximate Euler's number (e): "))
        if n >= 0:
            break
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Please enter a valid integer.")

e_approximation = euler_number_approximation(n)
print(f"Approximation of Euler's number (e) using {n} terms: {e_approximation:.10f}")

# Compare approximation with actual value
print(f"Actual value of Euler's number (e): {math.e:.10f}")
print(f"Absolute error: {abs(e_approximation - math.e):.10f}")


