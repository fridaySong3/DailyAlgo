# https://www.acmicpc.net/problem/1018
import sys

SIZE = 8
N, M = map(int, sys.stdin.readline().split())
change = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    s = sys.stdin.readline().strip()
    for m in range(M):
        if ((n + m) % 2 == 0 and s[m] == "B") or ((n + m) % 2 == 1 and s[m] == "W"):
            change[n][m] = 1

cnt = []
for n in range(N-SIZE+1):
    for m in range(M-SIZE+1):
        change_cnt = 0
        for i in range(SIZE):
            change_cnt += change[n+i][m:m+SIZE].count(1)
        cnt.append(change_cnt)

print( min(min(cnt), SIZE * SIZE - max(cnt)) )