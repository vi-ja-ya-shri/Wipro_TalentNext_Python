#  1. Add a key and value to a dictionary
dict={
    1:"Ram",
    2:"Seeta"
}
dict[3]="Reeta"
print(dict)

# 2. Concatenate the following dictionaries to create a new one
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic_res={**dic1,**dic2,**dic3}
print(dic_res)

# 3. Check if a given key already exists in a dictionary
my_dict = {1: 'a', 2: 'b', 3: 'c'}
k=2
if(k in my_dict):
    print("key is present")
else:
    print("key is absent")

# 4. Iterate over a dictionary using a for loop and print:
# Keys alone , Values alone , Both keys and values
my_dict = {1: 'a', 2: 'b', 3: 'c'}

# Keys
print("Keys:")
for key in my_dict:
    print(key)

# Values
print("Values:")
for value in my_dict.values():
    print(value)

# Keys and Values
print("Key-Value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

#  5. Prepare a dictionary where keys are numbers from 1 to 15 (both included) and values are squares of the keys
squares_dict = {x: x**2 for x in range(1, 16)}
print("Dictionary with squares:", squares_dict)

# 6. Sum all the values in a dictionary (values are integers)
my_dict = {1: 10, 2: 20, 3: 30}
total = sum(my_dict.values())
print("Sum of values:", total)