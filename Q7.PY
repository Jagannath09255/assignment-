def print_multiplication_table(number):
    multiplier = 1
    while multiplier <= 10:
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
        multiplier += 1

# Get input from the user
num = int(input("Enter a number to generate its multiplication table: "))

print(f"\nMultiplication Table for {num}:")
print_multiplication_table(num)