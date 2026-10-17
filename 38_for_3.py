numbers = [10, 15, 200, 7, 45, 90, -11, 125]

# --- Find Maximum Value and Its Index ---
max_val = numbers[0]
max_idx = 0

for index, value in enumerate(numbers):
    if value > max_val:
        max_val = value
        max_idx = index

print(f"Maximum Value : {max_val} and its position : {max_idx}")

# --- Find Minimum Value and Its Index ---
min_val = numbers[0]
min_idx = 0

for index, value in enumerate(numbers):
    if value < min_val:  # Check if the current value is smaller
        min_val = value
        min_idx = index

print(f"Minimum Value : {min_val} and its position : {min_idx}")