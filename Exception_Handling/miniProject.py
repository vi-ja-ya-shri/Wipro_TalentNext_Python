def process_purchase_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        item_count = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            line = line.strip()

            # Skip blank lines
            if not line:
                continue

            # Handle discount line separately
            if line.lower().startswith("discount"):
                try:
                    discount = float(line.split()[1])
                except (IndexError, ValueError):
                    print("Invalid discount format.")
                    continue
            else:
                parts = line.split()
                if len(parts) != 2:
                    print(f"Skipping invalid line: {line}")
                    continue
                item, price = parts[0], parts[1]
                try:
                    price = float(price)
                    item_count += 1
                    if price == 0:
                        free_items += 1
                    total_amount += price
                except ValueError:
                    print(f"Invalid price for item '{item}', skipping.")

        final_amount = total_amount - discount

        # Display result
        print(f"No of items purchased: {item_count}")
        print(f"No of free items: {free_items}")
        print(f"Total amount: {total_amount}")
        print(f"Discount: {discount}")
        print(f"Final amount to pay: {final_amount}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Take file name input from user
filename = input("Enter the file name: ")
process_purchase_file(filename)