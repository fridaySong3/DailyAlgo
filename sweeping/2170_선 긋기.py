# https://www.acmicpc.net/problem/2170
import sys
N = int(sys.stdin.readline())
lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
lines.sort()
ans = 0
start, end = lines[0]
for i in range(1, N):
    if end >= lines[i][0]:
        end = max(end, lines[i][1])
    else:
        ans += end - start
        start, end = lines[i]
ans += end - start
print(ans)