# 1. Division with Exception Handling
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(f"Result of division: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")

# 2. Check Prime Number with Exception Handling
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

try:
    num = int(input("Enter a number to check for prime: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")

#  3. Read File and Print Content in Title Case with Exception Handling
filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content in title case:")
        print(content.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# 4. Index Access with Exception Handling
numbers = [10, -3, 25, -7, 88, -42, 0, 15, -9, 31]

try:
    index = int(input("Enter an index (0–9): "))
    value = numbers[index]
    if value >= 0:
        print(f"The number at index {index} is positive: {value}")
    else:
        print(f"The number at index {index} is negative: {value}")
except IndexError:
    print("Error: Index out of range. Please enter a value between 0 and 9.")
except ValueError:
    print("Error: Invalid input. Please enter a numeric index.")