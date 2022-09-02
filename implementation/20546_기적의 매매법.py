# https://www.acmicpc.net/problem/20546
import sys
m1 = m2 = int(sys.stdin.readline())
prices = list(map(int, sys.stdin.readline().split()))
s1 = s2 = 0

for p in prices:
    s1 += m1 // p
    m1 %= p

up = down = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        up += 1
        down = 0
    elif prices[i] < prices[i-1]:
        down += 1
        up = 0
    else:
        up = down = 0
    if up == 3:
        m2 += s2 * prices[i]
        s2 = 0
    elif down >= 3:
        s2 += m2 // prices[i]
        m2 %= prices[i]

bnp = m1 + s1 * prices[-1]
timing = m2 + s2 * prices[-1]

if bnp > timing:
    print("BNP")
elif bnp < timing:
    print("TIMING")
else:
    print("SAMESAME")