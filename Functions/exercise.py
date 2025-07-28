# 1. Return the sum of all numbers in a list
def sum_of_list(numbers):
    return sum(numbers)

print(sum_of_list([8, 2, 3, 0, 7]))

#  2. Return the reverse of a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("1234abcd")) 

# 3. Return the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 

# 4. Count uppercase and lowercase letters in a string
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_case("HelloWorld") 

#  5. Print even numbers from a given list
def print_even_numbers(lst):
    evens = [x for x in lst if x % 2 == 0]
    print("Even numbers:", evens)

print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) 

# 6. Check whether a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))