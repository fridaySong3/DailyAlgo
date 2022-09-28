# https://www.acmicpc.net/problem/5212
import sys

R, C = map(int, sys.stdin.readline().split())
grid = [sys.stdin.readline().rstrip() for _ in range(R)]

d = ((-1, 0), (0, 1), (1, 0), (0, -1))
left_r = []
left_c = []
left_grid = [[False] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if grid[i][j] == '.':
            continue
        cnt_sea = 0
        for di, dj in d:
            ni, nj = i + di, j + dj
            if not (0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 'X'):
                cnt_sea += 1
        if cnt_sea < 3:
            left_r.append(i)
            left_c.append(j)
            left_grid[i][j] = True

for i in range(min(left_r), max(left_r)+1):
    for j in range(min(left_c), max(left_c)+1):
        if left_grid[i][j]:
            print('X', end='')
        else:
            print('.', end='')
    print()
