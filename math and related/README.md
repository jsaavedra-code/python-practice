# Factorial in Python

This program calculates the **factorial of a number** using Python.

## What is a Factorial?

A factorial is a mathematical operation.

The factorial of `n` (written as `n!`) is the product of all positive integers less than or equal to `n`.

Example:

5! = 5 × 4 × 3 × 2 × 1 = 120

## How the Program Works

1. The user enters an integer.
2. The program initializes `result = 1`.
3. A loop multiplies all numbers from `1` to `n`.
4. The program prints the final result.

## Example

Input
5

Output
120

## Python Code

```python
n = int(input())
result = 1

for i in range(1, n + 1):
    result *= i

print(result)

Author: John Saavedra
Computer Science Student