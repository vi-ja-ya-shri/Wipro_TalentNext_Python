#  1. Accept Two Numbers as Command Line Arguments and Display Their Sum
import sys

# Check if two numbers are passed
if len(sys.argv) != 3:
    print("Usage: python script.py <num1> <num2>")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}")

# 2. Accept a Welcome Message and Display the File Name and Message
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <welcome_message>")
else:
    script_name = sys.argv[0]
    welcome_message = " ".join(sys.argv[1:])
    print(f"Script Name: {script_name}")
    print(f"Welcome Message: {welcome_message}")

#  3. Accept 10 Numbers and Calculate Sum of Prime Numbers
import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Usage: python script.py <10_numbers>")
else:
    numbers = list(map(int, sys.argv[1:]))
    prime_sum = sum(num for num in numbers if is_prime(num))
    print(f"Sum of prime numbers: {prime_sum}")