# https://www.acmicpc.net/problem/1083
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline())
print(arr[:s])
if s != 0:
    for i in range(N-1):
        m, mi = max([(n, i+idx+1) for idx, n in enumerate(arr[i+1:i+1+s])])
        if arr[i] > m:
            continue
        for j in range(mi, i, -1):
            arr[j] = arr[j-1]
        arr[i] = m
        s -= mi - i
        if s == 0:
            break
print(" ".join(map(str, arr)))