# https://www.acmicpc.net/problem/1205
import sys
from bisect import bisect_left, bisect_right

N, sc, P = map(int, sys.stdin.readline().split())
if N == 0:
    print(1)
    exit()
    
scores = list(map(int, sys.stdin.readline().split()))
scores = list(reversed(scores))
i = bisect_left(scores, sc)

if i == len(scores):
    print(1)
elif sc < scores[i]:
    rank = len(scores) - i + 1
    if rank <= P:
        print(rank)
    else:
        print(-1)
else: # sc == scores[i]
    i = bisect_right(scores, sc)
    rank = len(scores) - i + 1
    if N == P and scores[0] == sc:
        print(-1)
    else:
        print(rank)
