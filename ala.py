# Bubble Sort Algorithm
# Algorithm Visualization & Complexity Analysis Lab

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred, list is already sorted
        if not swapped:
            break

    return arr


# Taking input from user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("\nOriginal List:", numbers)

# Applying Bubble Sort
sorted_numbers = bubble_sort(numbers)

print("Sorted List:", sorted_numbers)
