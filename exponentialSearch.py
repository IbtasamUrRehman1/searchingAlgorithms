def binarySearch(arr, target, low, high):
    while low <= high:
        mid = (low+high) //2
        mid_value = arr[mid]
        if mid_value == target:
            return mid # Target found return the index
        elif mid_value < target:
            low = mid + 1 # Discard the left half
        else:
            high = mid - 1 # Discard the right half
    return -1 # target not found


def exponentialSearch(arr, target):
    n = len(arr)
    if arr[0] == target:
        return 0 # target found at the first position
    i = 1
    while i < n and arr[i ] <= target:
        i *= 2
    # perform binary search within the found range
    return binarySearch(arr, target, i // 2, min(i , n - 1))

# example  array
my_list = [1,2,3,4,5,6,7]
target_vaue = 1

result = exponentialSearch(my_list, target_vaue)

if result != 1:
    print(f"Element {target_vaue} found at the index number :{ result}")
else:
    print(f" Element {target_vaue} not found in the list")








