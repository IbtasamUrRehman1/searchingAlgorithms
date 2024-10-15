import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def fibonacci_search(arr, x):
    n, fib_m2, fib_m1, fib_m = len(arr), 0, 1, 1
    while fib_m < n: fib_m2, fib_m1, fib_m = fib_m1, fib_m, fib_m1 + fib_m
    offset, steps = -1, []
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        steps.append((arr.copy(), i, x))
        if arr[i] < x:
            fib_m, fib_m1, fib_m2, offset = fib_m1, fib_m2, fib_m - fib_m1, i
        elif arr[i] > x:
            fib_m, fib_m1, fib_m2 = fib_m2, fib_m1 - fib_m2, fib_m - fib_m1
        else:
            steps.append((arr.copy(), i, x, True)); return i, steps
    if fib_m1 and arr[offset + 1] == x: steps.append((arr.copy(), offset + 1, x, True)); return offset + 1, steps
    return -1, steps
def update(frame):
    arr, pos, target, *found = frame
    plt.cla()
    plt.bar(range(len(arr)), arr, color='lightblue')
    plt.bar(pos, arr[pos], color='red')
    plt.axhline(y=target, color='green', linestyle='--')
    if found and found[0]:
        plt.title(f'Found target {target} at index {pos}')
    else:
        plt.title(f'Searching at index {pos}')
    plt.xlabel('Index')
    plt.ylabel('Value')
def animate_search(steps):
    fig = plt.figure(figsize=(8, 4))
    ani = FuncAnimation(fig, update, frames=steps, repeat=False, interval=1000)
    plt.show()
# Example
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85
index, search_steps = fibonacci_search(arr, x)
animate_search(search_steps)
print(f"Element found at index: {index}" if index != -1 else "Element not found")
