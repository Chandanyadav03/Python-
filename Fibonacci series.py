# 1. Using for Loop ----------------------------------------

n = int(input("Enter number: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 2. Using while Loop ------------------------------------

n = int(input("Enter number: "))
a, b = 0, 1
i = 0

while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1

# 3. Using Recursion -------------------------------------

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter number: "))

for i in range(n):
    print(fib(i), end=" ")

# 4. Using List (Store Series) --------------------------------

n = int(input("Enter number: "))

fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print(fib)

# 5. Using Lambda Function -----------------------------------------

from functools import reduce

n = int(input("Enter number: "))
fib = [0, 1]

for i in range(2, n):
    fib.append(fib[-1] + fib[-2])

print(fib)

# 6. Using Memoization (Optimized Recursion) --------------------------------------

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

n = int(input("Enter number: "))

for i in range(n):
    print(fib(i), end=" ")



