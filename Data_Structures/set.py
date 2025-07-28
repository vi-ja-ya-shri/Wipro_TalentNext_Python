# 1. Remove a given item from the set
my_set = {10, 20, 30, 40, 50}
item_to_remove = 30

my_set.discard(item_to_remove)  
print("Set after removal:", my_set)

# 2. Create an intersection of sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

intersection = set1 & set2 
print("Intersection:", intersection)

#  3. Create a union of sets
set1 = {10, 20, 30}
set2 = {30, 40, 50}

union = set1 | set2  # or set1.union(set2)
print("Union:", union)

# 4. Find the maximum and minimum value in a set
my_set = {5, 20, 15, 8, 30}

maximum = max(my_set)
minimum = min(my_set)

print("Maximum value:", maximum)
print("Minimum value:", minimum)