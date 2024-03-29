#iteracyjnie - Euklides
def gcd(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1

print(gcd(5, 25))

#rekurencyjnie
def gcd_recursive(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    while number2 != 0:
        return gcd_recursive(number2, number1 % number2)
    return number1

print(gcd_recursive(5, 25))

#nww
def lcm(number1, number2):
    return (number1 * number2) // gcd_recursive(number1, number2)  # // integer division

print(lcm(5, 25))