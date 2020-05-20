# %%
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smaller = [item for item in arr[1:] if item <= pivot]
        bigger = [item for item in arr[1:] if item > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(bigger)


# %%
print(quick_sort([10, 5, 3, 2]))
