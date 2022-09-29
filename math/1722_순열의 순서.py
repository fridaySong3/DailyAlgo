# https://www.acmicpc.net/problem/1722
import sys

def next_perm(perm):
    for i in range(N-1, 0, -1):
        if perm[i-1] < perm[i]:
            for j in range(N-1, i-1, -1):
                if perm[i-1] < perm[j]:
                    perm[i-1], perm[j] = perm[j], perm[i-1]
                    perm[i:] = list(reversed(perm[i:]))
                    break
            break

N = int(sys.stdin.readline())
code, *k_or_p = map(int, sys.stdin.readline().split())
perm = list(range(1, N+1))
if code == 1:
    k = k_or_p[0]
    for i in range(k-1):
        next_perm(perm)
    print(' '.join(map(str, perm)))
else:
    p = k_or_p
    cnt_k = 1
    while True:
        if perm == p:
            print(cnt_k)
            break
        next_perm(perm)
        cnt_k += 1