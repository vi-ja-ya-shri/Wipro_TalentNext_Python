#  1. Read the Entire Content of a TXT File and Display It
filename = "sample.txt"  # Change to your file name

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File Content:\n", content)
except FileNotFoundError:
    print("File not found.")

# 2. Read First n Lines from a TXT File (n as User Input)
filename = "sample.txt"

n = int(input("Enter number of lines to read: "))

try:
    with open(filename, 'r') as file:
        for i in range(n):
            line = file.readline()
            if line == '':
                break
            print(line, end='')
except FileNotFoundError:
    print("File not found.")

# 3. Accept Input from User and Append to TXT File
filename = "sample.txt"

user_input = input("Enter text to append to the file: ")

with open(filename, 'a') as file:
    file.write(user_input + '\n')

print("Text appended successfully.")

#  4. Read Contents Line by Line and Store in a List
filename = "sample.txt"

lines_list = []

try:
    with open(filename, 'r') as file:
        lines_list = [line.strip() for line in file]

    print("Lines stored in list:")
    print(lines_list)
except FileNotFoundError:
    print("File not found.")

# 5. Find the Longest Word from the TXT File
filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        words = file.read().split()
        longest = max(words, key=len)
        print("Longest word is:", longest)
except FileNotFoundError:
    print("File not found.")

# 6. Count Frequency of a User-Entered Word in a TXT File
filename = "sample.txt"

word_to_find = input("Enter the word to search in the file: ").lower()
count = 0

try:
    with open(filename, 'r') as file:
        content = file.read().lower()
        words = content.split()
        count = words.count(word_to_find)

    print(f"The word '{word_to_find}' occurred {count} time(s) in the file.")
except FileNotFoundError:
    print("File not found.")