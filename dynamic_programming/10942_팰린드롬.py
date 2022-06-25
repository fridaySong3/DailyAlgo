# https://www.acmicpc.net/problem/10942
import sys
N = int(sys.stdin.readline())
nums = [0 for _ in range(N+1)]
nums[1:] = list(map(int, sys.stdin.readline().split()))

len_p_odd = [0 for _ in range(N+1)]
for i in range(1,N+1):
    j = 1
    while i-j >= 1 and i+j <= N and nums[i-j] == nums[i+j]:
        len_p_odd[i] += 1
        j += 1

len_p_even = [0 for _ in range(N)]
for i in range(1,N):
    j = 0
    while i-j >= 1 and i+1+j <= N and nums[i-j] == nums[i+1+j]:
        len_p_even[i] += 1
        j += 1
    
M = int(sys.stdin.readline())
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    if (s + e) % 2 == 0:
        len_p = len_p_odd
        mid = int((s + e) / 2)
    else:
        len_p = len_p_even
        mid = (s + e) // 2
    if e <= mid + len_p[mid]:
        print(1)
    else:
        print(0)
    