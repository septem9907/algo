# %%
def binary_search(l, item):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if l[mid] == item:
            return mid
        elif l[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

# %%
# %%
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print(binary_search(my_list, -1))  # => None

