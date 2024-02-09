def interpoltationSearch(arr, x):
    low = 0
    high =len(arr) - 1

    while low <= high and arr[low] <= x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        # Estimate the position of the element
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low]) ))
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Example array
arr = [2,3,5,6,9,12,15,17]
x = 2 # X is the element we want to find in the above given array
result = interpoltationSearch(arr,x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print(f"Elemenet {x} is not present in the given array")







