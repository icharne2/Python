# Iteratively
def factorial_iterative(number):
    result = 1
    number = int(number)
    if number == 1:
        return 1
    else:
        for i in range(2, number + 1):
            result *= i
    return result

print(factorial_iterative(5))

# Recursively
def factorial_recursive(number):
    number = int(number)
    if number == 1:
        return 1
    else:
        return number * factorial_recursive(number - 1)

print(factorial_recursive(5))

# Recursively2
def factorial_recursive_2(n): return n * factorial_recursive_2(n - 1) if n > 1 else 1

print(factorial_recursive_2(5))
