# https://www.acmicpc.net/problem/1722
from operator import mul
import sys
from itertools import accumulate

N = int(sys.stdin.readline())
code, *k_or_p = map(int, sys.stdin.readline().split())

fac = list(reversed(list(accumulate(range(1, N), mul))))
cnt_small = [0] * (N-1)
if code == 1:
    k = k_or_p[0]
    q = k - 1
    for i in range(N-1):
        q, r = divmod(q, fac[i])
        cnt_small[i] = q
        if r == 0:
            break
        q = r
    perm = []
    sorted_p = list(range(1, N+1))
    for i in range(N-1):
        perm.append(sorted_p[cnt_small[i]])
        del sorted_p[cnt_small[i]]
    perm.append(sorted_p[0])
    print(' '.join(map(str, perm)))
else:  
    perm = k_or_p
    for i in range(N-1):
        for j in range(i+1, N):
            if perm[i] > perm[j]:
                cnt_small[i] += 1
    k = sum([cnt * f for cnt, f in zip(cnt_small, fac)]) + 1
    print(k)