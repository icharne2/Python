# Recursively
def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(5))

# Iteratively
def fibonacci_iterative(n):
    n = int(n)
    previous = 0
    next_num = 1
    for i in range(1, n + 1):
        print(next_num, end=" ")
        next_num += previous
        previous = next_num - previous

fibonacci_iterative(3)
