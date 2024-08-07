def print_numbers_skip_divisible_by_3():
    for number in range(1, 11):
        if number % 3 == 0:
            continue
        print(number)

print("Numbers from 1 to 10, skipping those divisible by 3:")
print_numbers_skip_divisible_by_3()