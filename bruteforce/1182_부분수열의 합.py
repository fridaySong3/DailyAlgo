# https://www.acmicpc.net/problem/1182
import sys

def bruteforce(idx, s):
    global ans
    if idx != 0 and s == S:
        ans += 1
    for i in range(idx, N):
        bruteforce(i + 1, s + arr[i])

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0
bruteforce(0, 0)
print(ans)