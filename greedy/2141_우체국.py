# https://www.acmicpc.net/problem/2141
import sys
from itertools import accumulate

N = int(sys.stdin.readline())
loc_num = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
loc_num.sort()
acc = [0]
acc.extend(list(accumulate([n for _, n in loc_num])))
half = acc[-1] // 2 + acc[-1] % 2
for i in range(len(acc)):
    if acc[i] >= half:
        print(loc_num[i-1][0])
        break