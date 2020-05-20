# %%
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# %%
import collections

# %%
l = [3, 3, 3, 3, 3, 1, 3]
cnt = collections.defaultdict(list)

# %%
for i, size in enumerate(l):
    cnt[size].append(i)


# %%
cnt

# %%
cnt = 0
nums = [1, 23, 52]
n = len([1 for item in nums if len(str(item)) % 2 == 0])

# %


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = {'L': 0, 'R': 0}
        cnt = 0
        for item in s:
            if item == 'L':
                d['L'] += 1
            else:
                d['R'] += 1
            if d['L'] == d['R']:
                cnt += 1
                d['L'] = d['R'] = 0
        return cnt

# %%
