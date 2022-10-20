# https://www.acmicpc.net/problem/5671
import sys

M = 5000
dp = [0] * (M+1)

for n in range(1, M+1):
    sn = str(n)
    if len(sn) == len(set(sn)):
        dp[n] = dp[n-1] + 1
    else:
        dp[n] = dp[n-1]

while True:
    try:
        N, M = map(int, sys.stdin.readline().split())
    except:
        break
    else:
        print(dp[M] - dp[N-1])