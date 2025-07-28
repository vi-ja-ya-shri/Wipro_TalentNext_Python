# Project_1
import random

# Step 1: Create initial dictionary
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Step 2: Display original dictionary
print("Initial Facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

# Step 3: Modify a fact
people_facts["Jeff"] = "Is afraid of heights."

# Step 4: Add a new person
people_facts["Jill"] = "Can hula dance."

# Step 5: Shuffle and display updated dictionary
print("\nUpdated Facts:\n")
# Convert to list, shuffle, then print to observe if order changes
items = list(people_facts.items())
random.shuffle(items)

for person, fact in items:
    print(f"{person}: {fact}")

# Project_2
# Sample input list
scores = [2, 3, 6, 6, 5]

max_score = max(scores)

filtered_scores = [score for score in scores if score != max_score]

runner_up = max(filtered_scores)

print("Runner-up score:", runner_up)

# Project_3

student_records = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

student_name = input("Enter a name: ")


if student_name in student_records:
    marks = student_records[student_name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark: {int(average)}")
else:
    print("Student not found.")

# Project_4
# Get input string from user
text = input("Enter the string: ")

# Count occurrences of the word "Alex"
count = text.count("Alex")

# Print result
print("Sample output:", count)