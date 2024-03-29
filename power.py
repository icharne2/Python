#iteracyjnie
def power_iterative(number, n):
    result = number
    for i in range(1, n):
        result *= number
    return result

print(power_iterative(2, 2))

#Rekurencyjnie
def power_recursive(number, n):
    if n == 1:
        return number
    else:
        return number * power_recursive(number, n - 1)

print(power_recursive(2, 2))

