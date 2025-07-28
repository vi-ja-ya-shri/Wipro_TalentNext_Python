def count_alex_occurrences(text):
    return text.count("Alex")

# Example input
input_string = "Hi Alex WelcomeAlex Bye Alex."
result = count_alex_occurrences(input_string)
print(result)

def calculate_bill(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        items = []
        total_amount = 0
        free_items = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.lower().startswith("discount"):
                try:
                    discount = int(line.split()[1])
                except (IndexError, ValueError):
                    print("Invalid discount format.")
            else:
                try:
                    name, price = line.split()
                    price = int(price)
                    total_amount += price
                    items.append((name, price))
                except ValueError:
                    print(f"Skipping invalid line: {line}")

        print(f"No of items purchased: {len(items)}")
        print(f"No of free items: {free_items}")
        print(f"Total amount: {total_amount}")
        print(f"Discount amount: {discount}")
        print(f"Final amount after discount: {total_amount - discount}")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
filename = input("Enter the file name: ")
calculate_bill(filename)

from collections import Counter

def find_meeting_info(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        line_count = len(lines)
        hour = line_count if line_count <= 12 else line_count - 12
        meridiem = "AM" if line_count <= 12 else "PM"

        # Count words
        words = []
        for line in lines:
            words.extend(line.strip().lower().split())

        word_counts = Counter(words)
        meeting_word, freq = word_counts.most_common(1)[0]
        meeting_place = meeting_word.capitalize() + " Street"

        print(f"Meeting time: {hour} {meridiem}")
        print(f"Meeting place: {meeting_place}")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

# Run the function
filename = input("Enter file name: ")
find_meeting_info(filename)