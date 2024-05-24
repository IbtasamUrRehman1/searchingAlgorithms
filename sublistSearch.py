import matplotlib.pyplot as plt

def sublist_Search(main_list, sub_list):
    m = len(main_list)
    n = len(sub_list)

    for i in range(m - n + 1):
        if main_list[i:i + n] == sub_list:
            return i
    return -1

def visualization_sublist_search(main_list, sub_list):
    fig, ax = plt.subplots()

    def plot_array(arr, start_idx=None, end_idex = None, match=False):
        ax.clear()
        colors = ['blue'] * len(arr)
        if start_idx is not None and end_idex is not None:
            for i in range(start_idx, end_idex):
                colors[i] = 'green' if match else 'red'
        ax.bar(range(len(arr)), arr, color=colors)

        if match:
            ax.text(start_idx + n / 2 - 0.5, max(arr), 'Match Found', color='green', fontsize=12, ha='center')
        plt.pause(1)

    m = len(main_list)
    n = len(sub_list)


    for i in range( m - n + 1):
        plot_array(main_list, i, i + n)
        if main_list[i:i + n] == sub_list:
            plot_array(main_list, i, i + n, match=True)
            return i
    plot_array(main_list)
    return -1

# Example
main_list = [1,2,3,4,5,6,7,8,9]
sub_list = [4,5,6]
index = visualization_sublist_search(main_list, sub_list)
plt.show()
















