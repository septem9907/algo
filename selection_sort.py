# %%
def selection_sort(arr):
    for i in range(len(arr)):
        idx_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx_min]:
                idx_min = j
                arr[j], arr[i] = arr[i], arr[j]
    return arr

# %%
print(selection_sort([5, 3, 6, 2, 10]))

# %%
print(selection_sort([5, 5, 3, 9, 9, 2, 10]))

# %%
