# %%

# %%
# 1. Anagram Check

def anagram(s1, s2):

    def count_char(s):
        sl = s.lower()
        d = {}
        for item in sl:
            if item == ' ':
                continue
            else:
                if item in d.keys():
                    d[item] += 1
                else:
                    d[item] = 1
        return d

    d1 = count_char(s1)
    d2 = count_char(s2)

    if d1 == d2:
        return True
    else:
        return False

# %%
anagram("public relations", "crap built on lies")

anagram('clint eastwood', 'old west action')

# %%
# 2. Arrary Pair Sum

def pair_sum(arr, k):
    if len(arr) < 2:
        return 0
    
    l_pair = []
    for idx, val in enumerate(arr):
        if idx == len(arr) - 1:
            break
        if (k - val) in arr[(idx + 1):]:
            l_pair.append([val, k - val])
    
    return len(set(l_pair))

# %%
def pair_sum(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k - num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        else:
            # Add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target))) 
    
    # FOR TESTING
    return len(output)

# %%
pair_sum([1,3,2,2, 3, 1], 4)

# %%
# 3. Find the Missing Element
def finder(arr1, arr2):
    return sum(arr1) - sum(arr2)

# %%
