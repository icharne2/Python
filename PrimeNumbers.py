def is_prime(number):
    number = int(number)
    if number == 2:
        return True
    if number % 2 == 0 or number < 2:
        return False

    limit = int(number / 2) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False
    return True

if is_prime(5):
    print("Prime number")
else:
    print("It's not a prime number")
