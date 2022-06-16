# https://www.acmicpc.net/problem/2098
# DP, bitmask, TSP
import sys

def remove(visited, node):
    return visited & ~(1<<node)

def dfs(start, visit):
    if visit == 0: # if path is 'start -> end'
        return W[start][end] if W[start][end] != 0 else INF
    
    if dp[start][visit] != INF: # if already calculated
        return dp[start][visit]
        
    for i in range(N):
        if visit & (1<<i) == 0: # if i is not in visit
            continue
        if W[start][i] == 0: # if there are no path 'start -> i'
            continue
        dp[start][visit] = min(dp[start][visit], dfs(i, remove(visit, i)) + W[start][i])
    return dp[start][visit]

N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

INF = (1<<31) - 1
dp = [[INF] * (1<<N) for _ in range(N)] # dfs[i][j]: min_weight of path (i -> path(represented by binary j) -> end)
end = 0
all_visit = (1<<N) - 1
print(dfs( end, remove(all_visit, end) ))