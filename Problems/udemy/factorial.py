
def factorial(n):
    fact = 1
    if n > 0:
        for i in range(1, n + 1):
            fact *= i
    else: return 1

    return fact

print(factorial(5))
print(factorial(8))
print(factorial(10))

