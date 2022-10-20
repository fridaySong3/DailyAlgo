# https://www.acmicpc.net/problem/1246
import sys
N, M = map(int, sys.stdin.readline().split())
prices = [int(sys.stdin.readline()) for _ in range(M)]
prices.sort()
price = 0
max_profit = 0
m = M
for p in prices:
    profit = p * min(N, m)
    if max_profit < profit:
        max_profit = profit
        price = p
    m -= 1
print(price, max_profit)