# This program calculates the factorial of a given number n.

n = int(input())
result = 1
for i in range(1, n + 1):
    result *= i 
print(result)

