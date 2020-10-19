# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# %%
def solution(A, K):
    # write your code in Python 3.6
    N = len(A)
    if N == 0:
        return []
    else:
        if N >= K:
            return A[-K:] + A[0:-K]
        else:
            k = K % N
            return A[-k:] + A[0:-k]

# %%
A = [9, 8, 9]

d = {}
for elem in A:
    if elem in d.keys():
        d[elem] += 1
    else:
        d[elem] = 1

for k, v in d.items():
    if v == 1:
        return k

# %%
N = 5
s = set(range(1, N+1))
# %%
s2 = set([1, 2, 3, 4, 6])
# %%
a = s.difference(s2)
# %%
a.pop()
# %%
x = a.pop()
# %%
type(x)
# %%
A = [2, [1, 3]]
# %%
A[:]
# %%
