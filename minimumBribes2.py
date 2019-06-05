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
        n_less = sum([1 for j in range(1, n) if q[j] < q[0]])
        cnt = n_less
        for i in range(1, n):
            if q[i] > q[i - 1] and q[i - 1] > max(q):
                cnt += n_less
            else:
                if i > (n / 2):
                    n_less = sum([1 for j in range(i + 1, n) if q[j] < q[i]])
                    cnt += n_less
                else:
                    n_less = i + 1 - sum([1 for j in range(i) if q[j] < q[i]])
                    cnt += n_less
        print(cnt)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
