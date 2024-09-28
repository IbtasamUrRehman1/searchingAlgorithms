import math
import matplotlib.pyplot as plt
import time


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Visualization setup
    plt.ion()
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='lightblue')
    ax.set_title('Jump Search Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    # Jump Search Algorithm
    while prev < n and arr[min(step, n) - 1] < target:
        for bar in bars:
            bar.set_color('lightblue')
        for j in range(prev, min(step, n)):  # Update bars color within range
            bars[j].set_color('orange')
        plt.draw()
        plt.pause(0.5)
        prev = step
        step += int(math.sqrt(n))

    for bar in bars:
        bar.set_color('lightblue')
    for j in range(prev, min(step, n)):  # Update bars color within range
        bars[j].set_color('orange')
    plt.draw()
    plt.pause(0.5)

    for i in range(prev, min(step, n)):
        bars[i].set_color('red')
        plt.draw()
        plt.pause(0.5)
        if arr[i] == target:
            bars[i].set_color('green')
            plt.draw()
            plt.pause(0.5)
            plt.ioff()
            plt.show()
            return i

    plt.ioff()
    plt.show()
    return -1


# Example
arr = [i for i in range(1, 21)]
target = 15
result = jump_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array.")
