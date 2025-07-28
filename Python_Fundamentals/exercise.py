#  1. Check if a number is Positive, Negative, or Zero
num=int(input("enter a number "))
def checkNum(num):
    if(num>0):
        return "Positive"
    elif(num<0):
        return "Negative"
    else:
        return "Zero"
print(checkNum(num))

# 2. Check if a number is Odd or Even
def check_Even_Odd(num):
    if(num % 2 ==0):
        print("Even")
    else:
        print("Odd")
print(check_Even_Odd(num))

# 3. Check if two numbers have the same last digit
def check_LastDigit(num1,num2):
    if(num1 % 10 == num2 % 10):
        return True
    else:
        return False
print(check_LastDigit(12,133))

# 4. Print numbers from 1 to 10 in a single row with tab space
def printNumbers():
    for num in range(1,11):
       print(num ,end='\t')
print(printNumbers())

#  5. Print even numbers between 23 and 57 (each on a new line)
def print_Even():
    for num in range(23,57):
        if(num % 2==0):
            print(num)
print(print_Even())

# # 6. Check if a number is Prime
def check_Prime(num):
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            return False
    else:
        return True
print(check_Prime(1100))

# # 7. Print prime numbers between 10 and 99
def PrintPrime():
    for i in range(10,100):
        if(check_Prime(i)):
            print(i)
print(PrintPrime())

#  8. Print the sum of all digits of a number
def DigitSum(num):
    sum=0
    while(num>0):
        sum+=num%10
        num=num//10
    print(sum)
print(DigitSum(12345))

# 9. Reverse a given number
def Reverse(num):
    ans=0
    while(num>0):
        ans=ans*10+num%10
        num=num//10
    print("Reversed num ",ans)
print(Reverse(12345))

# 10. Check whether a given number is a palindrome or not
def check_Palindrome(num):
    original=num
    ans=0
    while(num>0):
        ans=ans*10+num%10
        num=num//10

    if(ans==original):
        print("Palindrome")
    else:
        print("Not a Palindrome")
print(check_Palindrome(12213))