# https://www.acmicpc.net/problem/15486
import sys
N = int(sys.stdin.readline())
T = [0 for _ in range(N)]
P = [0 for _ in range(N)]
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T[i] = t
    P[i] = p

dp = [0 for _ in range(N+1)]
for i in range(N-1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])