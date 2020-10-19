# %%
# 1. Reverse a String

def reverse(s):
    if len(s) > 1:
        return reverse(s[1:]) + s[0]
    else:
        return s[0]

# %%
print(reverse('123456789'))

# %%
# 2. String Permutation

def permute(s):

    if len(s) <= 1:
        return [s]
    else:
        l = []
        for idx, val in enumerate(s):
            l_temp = permute(s[0:idx]+s[idx+1:])
            l += [val + item for item in l_temp]
        return l

# %%
permute('xxx')

# %%
# 3. Fibonnaci Sequence

def fib_rec(n):
    if n <= 2:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

# %%
print(fib_rec(23))

# %%
d = {}
def fib_dyn(n):
    if n <= 2:
        return 1
    else:
        if n not in d:
            d[n] = fib_dyn(n - 1) + fib_dyn(n - 2) 
        return d[n]

# %%
print(fib_dyn(23))

# %%
def fib_iter(n):
    if n <= 2:
        return 1
    else:
        arr = []
        for i in range(n):
            if i < 2:
                arr.append(1)
            else:
                arr.append(arr[i - 2] + arr[i - 1])
        return arr[n - 1]

# %%
print(fib_iter(23))

# %%
# 4. Coin Change

def rec_coin(target, coins):

    if target in coins:
        return 1
    else:
        
        n_min = target

        for item in [c for c in coins if c <= target]:
            
            target_new = target - item

            n_item = rec_coin(target_new, coins) + 1

            if n_item < n_min:
                n_min = n_item
            
        return n_min

# %%
rec_coin(10, [1, 5])
