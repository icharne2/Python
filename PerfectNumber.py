def is_perfect(number):
    sum_of_divisors = 1
    limit = int(number / 2) + 1
    for i in range(2, limit):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors

print("Enter a number")
number = input()
number = int(number)

if is_perfect(number) == number:
    print("This number is perfect!")
else:
    print("It's not perfect :<")

