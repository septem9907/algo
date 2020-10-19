# %%
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0
    
    B = [0] * len(A)
    
    for i in range(len(A)-1):
        if A[i] >= A[i + 1]:
            continue
        else:
            B[i] = max(max(A[i+1:]) - A[i], 0)
    
    return max(B)


# %%
A = [3, 2, -6, 4, 0]

N = 24

l = [1, N]
i = 2
while i < int(N / 2):
    
    if (N % i == 0):
        l.append(i)
        if i != int(N / i):
            l.append(int(N / i))
    
    if (i >= int(N / i)):
        break
    
    i += 1

# %%
N = 10
M = 4

X = 0

l_wrapper = []

while X not in l_wrapper:
    l_wrapper.append(X)
    X = (X + M) % 10

# %%
A = [1, 2, 1, 3, 3]

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution61(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0

    d = {}

    for item in A:
        if item in d.keys():
            d[item] += 1
        else:
            d[item] = 1
    
    return len(d.keys())

# %%
def solution64(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0
    else:
        A.sort()
        
        N = len(A)
        
        for i in range(N - 2):
            if A[i] + A[i + 1] > A[i + 2]:
                return 1
        
        return 0

# %%
def solution71(S):
    # write your code in Python 3.6
    stack = [] 
  
    # Traversing the Expression 
    for char in S: 
        if char in ["(", "{", "["]: 
  
            # Push the element in the stack 
            stack.append(char) 
        else: 
  
            # IF current character is not opening 
            # bracket, then it must be closing. 
            # So stack cannot be empty at this point. 
            if not stack: 
                return 0

            current_char = stack.pop() 
            if current_char == '(': 
                if char != ")": 
                    return 0
            if current_char == '{': 
                if char != "}": 
                    return 0
            if current_char == '[': 
                if char != "]": 
                    return 0
  
    # Check Empty Stack 
    if stack: 
        return 0
    return 1


# %%
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

# %%
def solution72(A, B):
    # write your code in Python 3.6
    l_down = []
    n_survival = 0

    for i in range(len(A)):
        if B[i] == 1:
            l_down.append(A[i])
        else:
            while len(l_down) > 0:
                if l_down[-1] > A[i]:
                    break
                else:
                    l_down.pop()
            else:
                n_survival += 1

    n_survival += len(l_down)
 
    return n_survival

# %%
def solution73(S):
    stack = []

    for item in S:
        if item == '(':
            stack.append(item)
        else:
            if not stack:
                return 0
            else:
                stack.pop()

    if stack:
        return 0
    else:
        return 1

# %%
def solution81(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return -1
        
    d = {}
    
    for item in A:
        if item in d.keys():
            d[item] += 1
        else:
            d[item] = 1
    
    max_val = max(d.values())
    
    if max_val <= int(len(A) / 2):
        return -1
    else:
        dominator = [k for k, v in d.items() if v == max_val][0]
        idx = A.index(dominator)
        return idx

# %%
def find_leader(A):

    if len(A) == 0:
        return 0
        
    d = {}
    
    for item in A:
        if item in d.keys():
            d[item] += 1
        else:
            d[item] = 1
    
    max_val = max(d.values())
    
    if max_val > int(len(A) / 2):
        leader = [k for k, v in d.items() if v == max_val][0]
        return leader
    else:
        return 0

# %%
A = [4, 3, 4, 4, 4, 2]
l = []
for idx in range(len(A) - 1):
    A1 = A[:idx+1]
    A2 = A[idx+1:]
    leader1 = find_leader(A1)
    leader2 = find_leader(A2)
    if (leader1 == leader2) and (leader1 > 0):
        l.append(idx)

len(l)

# %%
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    def find_leader(A):
        if len(A) == 0:
            return 0
            
        d = {}
        
        for item in A:
            if item in d.keys():
                d[item] += 1
            else:
                d[item] = 1
        
        max_val = max(d.values())
        
        if max_val > int(len(A) / 2):
            leader = [k for k, v in d.items() if v == max_val][0]
            return leader
        else:
            return 0

    # %%
    l = []
    for idx in range(len(A) - 1):
        A1 = A[:idx+1]
        A2 = A[idx+1:]
        leader1 = find_leader(A1)
        leader2 = find_leader(A2)
        if (leader1 == leader2) and (leader1 > 0):
            l.append(idx)

    return len(l)

# %%
def solution151(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0
        
    d = {}
    for item in A:
        if item < 0:
            if abs(item) not in d.keys():
                d[abs(item)] = 1
        else:
            if item not in d.keys():
                d[item] = 1
    return len(d.keys())

# %%
A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]

# %%
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution161(A, B):
    # write your code in Python 3.6
        # No overlapping is possible.
    if len(A) < 2:      
        return len(A)
    count = 1       # The first segment starts a new cluster.
    end = B[0]
    index = 1       # The second segment.
    while index < len(A):
        # Skip all the segments in this cluster.
        while index < len(A) and A[index] <= end:   
            index += 1
        # All segments are processed.
        if index == len(A):                         
            break
        # Start a new cluster.
        count += 1
        end = B[index]
    return count