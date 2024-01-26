def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return 1  # Return the index if the target is found
    return -1  # Return -1 if the target is not found in the given array


# Take input from user

my_List = [0, 7, 8, 5, 6, 8, 43]

target_value = int(input("Enter the target value to search for :"))

result = linearSearch(my_List, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}")
else:
    print(f"Element {target_value} not found in the list")
