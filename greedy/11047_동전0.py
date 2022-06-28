# https://www.acmicpc.net/problem/11047
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

idx = -1
for i in range(len(coins)):
    if coins[i] == K:
        print(1)
        exit()
    elif coins[i] > K:
        idx = i - 1
        break
if idx == -1:
    idx = len(coins) - 1
    
answer = 0
remain = K
for i in range(idx, -1, -1):
    answer += remain // coins[i]
    remain %= coins[i]
    if remain == 0:
        break
print(answer)