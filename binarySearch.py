def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # if the low pointer surpass the high poinerm the target is not in the list
    mid = (low + high) // 2
    mid_value = arr[mid]
    if mid_value == target:
        return mid  # target found, return the index
    elif mid_value < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    # recur on the right half, and discard the lef half
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
    # recur on the left halfm discard the right half


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# take the target value from the user
target_value = int(input("Enter the target value to search for: "))

# perform binary search using recursion and display the result
result = binary_search_recursive(my_list, target_value, 0, len(my_list) - 1)

if result != 1:
    print(f"Element {target_value} found at the index number: { result}")
else:
    print(f"Element {target_value}not found in the list")
