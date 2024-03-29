def factors(number):
    factors_list = []
    number = int(number)
    divisor = 2

    while number != 1:
        while number % divisor == 0:
            factors_list.append(divisor)
            number = int(number / divisor)
        divisor += 1
    print(factors_list)

factors(6)
