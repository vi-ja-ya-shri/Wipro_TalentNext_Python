# Project_1
def sort_colors(color_string):
    # Split the string by hyphen
    colors = color_string.split('-')
    # Sort the list alphabetically
    colors.sort()
    
    return '-'.join(colors)


input_string = "green-red-yellow-black-white"
output_string = sort_colors(input_string)
print(output_string)



#  Project_2


def ispalindrome(name):
    return name == name[::-1]

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in name if char in vowels)

def frequency_of_letters(name):
    freq = {}
    for char in name:
        freq[char] = freq.get(char, 0) + 1
    return freq

# test



name = "bob"

# Test ispalindrome
if ispalindrome(name):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")

# Test count_the_vowels
vowel_count = count_the_vowels(name)
print(f"No of vowels: {vowel_count}")

# Test frequency_of_letters
freq = frequency_of_letters(name)
freq_output = ", ".join([f"{char}-{count}" for char, count in freq.items()])
print(f"Frequency of letters: {freq_output}")
