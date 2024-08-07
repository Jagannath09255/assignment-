def print_numbers_until_greater_than_5():
    numbers = [1, 3, 5, 7, 2, 4, 6, 8]
    print("Printing numbers until a number greater than 5 is encountered:")
    for number in numbers:
        if number > 5:
            print(f"Encountered {number}, which is greater than 5. Stopping.")
            break
        print(number)

print_numbers_until_greater_than_5()