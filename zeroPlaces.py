def function(x):
    # f(x) = x^3 - 3x^2 + 2x - 6
    return x * (x * (x - 3) + 2) - 6

def find_zero(a, b, epsilon):
    if function(a) == 0.0:
        return a
    if function(b) == 0.0:
        return b

    while b - a > epsilon:
        x = (a + b) / 2
        if x == 0.0:
            return x
        if function(a) * function(x) < 0:
            b = x
        else:
            a = x
    return (a + b) / 2

print(find_zero(-10, 10, 0.00001))
