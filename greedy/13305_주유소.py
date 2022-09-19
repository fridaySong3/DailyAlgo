# https://www.acmicpc.net/problem/13305
import sys
from itertools import accumulate

N = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
del price[-1]
remain_d = reversed(list(accumulate(reversed(d))))
arr = sorted(zip(price, remain_d))
distance = arr[-1][1]
prev_r_d = 0
ans = 0
for p, r_d in arr:
    if r_d < prev_r_d:
        continue
    rr_d = r_d - prev_r_d
    ans += p * rr_d
    distance -= rr_d
    if distance == 0:
        break
    prev_r_d = r_d
print(ans)