def give_change(change):
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    while change:
        for denomination in denominations:
            if change - denomination >= 0:
                print(denomination)
                change -= denomination

print("Enter the change:")
change_input = input()

print("Dispensed banknotes:")
give_change(int(change_input))
