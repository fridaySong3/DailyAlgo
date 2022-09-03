N = int(input())
M = int(input())

vip = [0]
vip.extend([int(input()) for _ in range(M)])

if M == 0:
    length = [N]
else:
    length = [vip[i] - vip[i-1] - 1 for i in range(1, M+1)]
    length.append(N - vip[M])

long = max(length)
dp = [[0 for _ in range(long//2+1)] for _ in range(long+1)]
for i in range(0, long+1):
    dp[i][0] = 1

for i in range(2, long+1):
    for j in range(1, i//2+1):
        dp[i][j] = dp[i-1][j] + dp[i-2][j-1]

ans = 1
for l in length:
    ans *= sum(dp[l])
print(ans)