# https://www.acmicpc.net/problem/16206
import sys
base = 10
N, M = map(int, sys.stdin.readline().split())
length = list(map(int, sys.stdin.readline().split()))
ans = 0
h_priority = []
l_priority = []
for l in length:
    if l == base:
        ans += 1
    elif l % base == 0:
        h_priority.append(l)
    else:
        l_priority.append(l)
h_priority.sort()
for l in h_priority:
    cake_num = l // base
    cut_num = cake_num - 1
    if cut_num <= M:
        ans += cake_num
        M -= cut_num
    else:
        ans += M
        M = 0
    if M == 0:
        break
if M != 0:
    cake_num = 0
    for l in l_priority:
        cake_num += l // base
        if cake_num >= M:
            ans += M
            M = 0
            break
    if M != 0:
        ans += cake_num
print(ans)