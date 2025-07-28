#  1. Print the 4th element from the first and 4th from the last in a tuple
t = (10, 20, 30, 40, 50, 60, 70, 80)

# 4th element from the start (index 3)
print("4th from start:", t[3])

# 4th element from the end (index -4)
print("4th from end:", t[-4])

# 2. Check whether an element exists in a tuple
t = (1, 2, 3, 4, 5)
element = 3

if element in t:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

# 3. Convert a list into a tuple

my_list = [10, 20, 30, 40]
my_tuple = tuple(my_list)
print("Converted tuple:", my_tuple)

#  4. Find the index of an item in a tuple
t = (10, 20, 30, 40, 50)
item = 30

index = t.index(item)
print(f"Index of {item} is {index}")

#  5. Replace the last value of each tuple in a list to 100
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# Replace last element of each tuple with 100
modified_list = [t[:-1] + (100,) for t in sample_list]

print("Modified list:", modified_list)
