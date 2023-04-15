# https://www.acmicpc.net/problem/2206
import sys

def print_grid(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            print(grid[r][c], end = " ")
        print()
        
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
path = set() # (r, c)
visit = set() # (r, c, direction_index(0~3))

def dfs(grid, dp, loc, break_wall):
    r, c, _ = loc
    if dp[r][c] != None:
        return dp[r][c]
    if (r, c) in path or loc in visit:
        return -1
    path.add((r, c))
    visit.add(loc)
    
    # print(r, c)
    
    min_d = float('inf')
    for i in range(len(dr)):
        nr = r + dr[i]
        nc = c + dc[i]
        d = None
        if grid[nr][nc] == 1 and not break_wall:
            d = dfs(grid, dp, (nr, nc, i), True) + 1
        elif grid[nr][nc] == 0:
            d = dfs(grid, dp, (nr, nc, i), False) + 1
        
        if d != None and d != -1 and min_d > d:
            min_d = d
    
    path.remove((r, c))
    dp[r][c] = min_d if min_d != float('inf') else -1
    return dp[r][c]

# 입력
R, C = map(int, sys.stdin.readline().split())
grid = [[None for _ in range(C+2)] for _ in range(R+2)]
for r in range(1, R+1):
    grid[r][1:C+1] = map(int, list(sys.stdin.readline().strip()))
# print_grid(grid)

dp = [[None for _ in range(C+2)] for _ in range(R+2)]
dp[1][1] = 1
print(dfs(grid, dp, (R, C, 0), False))
            