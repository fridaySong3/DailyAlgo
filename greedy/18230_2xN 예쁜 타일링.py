# https://www.acmicpc.net/problem/18230
import sys
n, a, b = map(int, sys.stdin.readline().split())
t1 = list(map(int, sys.stdin.readline().split()))
t2 = list(map(int, sys.stdin.readline().split()))
t1.sort(reverse=True)
t2.sort(reverse=True)
ans = 0
i1, i2 = 0, 0
if n % 2 == 1:
    n -= 1
    ans += t1[i1]
    i1 += 1
for _ in range(0, n, 2):
    p1, p2 = 0, 0
    if i1 < len(t1) - 1:
        p1 = t1[i1] + t1[i1+1]
    if i2 < len(t2):
        p2 = t2[i2]
    
    if p1 > p2:
        ans += p1
        i1 += 2
    else:
        ans += p2
        i2 += 1

print(ans)