# https://www.acmicpc.net/problem/1051
import sys

N, M = map(int, sys.stdin.readline().split())
grid = [[[False] * M for _ in range(N)] for _ in range(10)]
point = [[[] for _ in range(N)] for _ in range(10)]
for r in range(N):
    for c, num in enumerate(map(int, list(sys.stdin.readline().rstrip()))):
        grid[num][r][c] = True
        point[num][r].append(c)
ans = 0
for n in range(len(point)):
    for r1 in range(len(point[n])):
        for ci in range(len(point[n][r1])-1):
            for cj in range(ci+1, len(point[n][r1])):
                c1, c2 = point[n][r1][ci], point[n][r1][cj]
                len_h = c2 - c1
                r2 = r1 + len_h
                if r2 < N and grid[n][r2][c1] and grid[n][r2][c2]:
                    ans = max(ans, len_h)
            
print((ans+1)**2)