#  1. Count number of uppercase and lowercase letters in a string
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_case("HelloWorld")

# 2. Check whether a string is a palindrome

def is_palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

is_palindrome("madam")
is_palindrome("python")

# 3. Return a string made of n copies of the first 2 chars, where n = len(string)

def repeat_front(s):
    n = len(s)
    result = s[:2] * n
    print(result)

repeat_front("Wipro") 

#4. If first or last char is 'x', return the string without those 'x', else unchanged
def remove_x(s):
    if s.startswith('x'):
        s = s[1:]
    if s.endswith('x'):
        s = s[:-1]
    print(s)

remove_x("xHix")  
remove_x("Hello")  

# 5. Given string and integer n, repeat last n characters n times
def repeat_last_n(s, n):
    substring = s[-n:]
    result = substring * n
    print(result)

repeat_last_n("Wipro", 3)  # Output: propropro