# https://www.acmicpc.net/problem/2302
N = int(input())
M = int(input())

dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 1
for i in range(2, len(dp)):
    dp[i] = dp[i-2] + dp[i-1]

if M == 0:
    print(dp[N])
else:
    ans = 1
    prev = 0
    for _ in range(M):
        vip = int(input())
        ans *= dp[vip - prev - 1]
        prev = vip
    ans *= dp[N - prev]
    print(ans)