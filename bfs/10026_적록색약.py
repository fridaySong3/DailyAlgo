# https://www.acmicpc.net/problem/10026
import sys
from collections import deque

def is_same_1(grid, r1, c1, r2, c2):
    return grid[r1][c1] == grid[r2][c2]

def is_same_2(grid, r1, c1, r2, c2):
    return grid[r1][c1] == grid[r2][c2] or (grid[r1][c1], grid[r2][c2]) in {("R", "G"), ("G", "R")}

drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

def bfs(grid, not_visit, is_same):
    for n in not_visit:
        r, c = n
        break
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        if (r, c) in not_visit:
            not_visit.remove((r, c))
            for dr, dc in zip(drs, dcs):
                nr = r + dr
                nc = c + dc
                if is_same(grid, r, c, nr, nc) and (nr, nc) in not_visit:
                    queue.append((nr, nc))

N = int(sys.stdin.readline())

grid = [[None for _ in range(N+2)] for _ in range(N+2)]
for r in range(1, N+1):
    grid[r][1:N+1] = list(sys.stdin.readline().strip())

not_visit = {(r, c) for r in range(1, N+1) for c in range(1, N+1)}
answer1 = 0
while not_visit:
    answer1 += 1
    bfs(grid, not_visit, is_same_1)
    
not_visit = {(r, c) for r in range(1, N+1) for c in range(1, N+1)}
answer2 = 0
while not_visit:
    answer2 += 1
    bfs(grid, not_visit, is_same_2)

print(answer1, answer2)