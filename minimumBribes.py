#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    l_index = list(range(n))
    l = [(i - 1) - j for i, j in zip(q, l_index)]

    if max(l) > 2:
        print("Too chaotic")
    else:
        cnt = 0
        for i in range(n):
            cnt += sum([1 for j in range(i + 1, n) if q[j] < q[i]])
        print(cnt)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
