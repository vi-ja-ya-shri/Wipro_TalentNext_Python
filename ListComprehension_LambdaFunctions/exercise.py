# Lambda Functions
# 1. Cube every number in a list using Lambda
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cubes = list(map(lambda x: x**3, list_1))
print(cubes)



# List Comprehension
# 2. Dictionary with only odd numbers as keys and their cubes as values (using LC)
input_list = [1, 2, 3, 4, 5, 6, 7]

output_dict = {x: x**3 for x in input_list if x % 2 != 0}
print(output_dict)




# 3. Dictionary of English alphabets with corresponding integer
import string

alphabet_dict = {ch: idx+1 for idx, ch in enumerate(string.ascii_lowercase)}
print(alphabet_dict)

