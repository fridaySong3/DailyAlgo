# https://www.acmicpc.net/problem/20950
import sys

def dfs(idx, k, sum_color):
    global ans
    if k > 7:
        return
    if idx == N:
        if k > 1:
            avg = [c//k for c in sum_color]
            ans = min(ans, sum([abs(b - a) for b, a in zip(base, avg)]))
        return
    dfs(idx + 1, k + 1, [s + c for s, c in zip(sum_color, colors[idx])])
    dfs(idx + 1, k, sum_color)
    
N = int(sys.stdin.readline())
colors = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
base = list(map(int, sys.stdin.readline().split()))
ans = 255 * 3
dfs(0, 0, [0, 0, 0])
print(ans)