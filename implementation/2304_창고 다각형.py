# https://www.acmicpc.net/problem/2304
import sys

def find_ge(h, LH, beg, end):
    for i in range(beg, end):
        if h <= LH[i][1]:
            return i
    return -1

N = int(sys.stdin.readline())

LH = [None for _ in range(N)]
for i in range(N):
    LH[i] = tuple(map(int, sys.stdin.readline().split()))

if N == 1:
    print(LH[0][1])
    exit()
    
LH.sort()

prev = 0
here = 1
while here < (len(LH)-1) :
    if LH[prev][1] >= LH[here][1]:
        j = find_ge(LH[here][1], LH, here+1, len(LH))
        if j > 0:
            del LH[here:j]
            continue
    prev = here
    here += 1

ans = 0
for i in range(len(LH)-1):
    ans += LH[i][1]
    ans += (LH[i+1][0] - LH[i][0] - 1) * min(LH[i][1], LH[i+1][1])
ans += LH[-1][1]
    
print(ans)