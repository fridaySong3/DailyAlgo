# https://www.acmicpc.net/problem/1689
import sys
N = int(sys.stdin.readline())
lines = [None] * (2 * N)
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    lines[i] = (s, 1)
    lines[i+N] = (e, -1)
lines.sort()

ans = 0
cnt = 0
for i in range(2 * N):
    cnt += lines[i][1]
    ans = max(ans, cnt)
print(ans)