# https://www.acmicpc.net/problem/1189
import sys
R, C, K = map(int, sys.stdin.readline().split())
m = [[None for _ in range(C+2)] for _ in range(R+2)]
for r in range(1, R+1):
    m[r][1:C+1] = list(sys.stdin.readline().rstrip())

def go(r, c, d):
    global ans
    if d == K:
        if r == 1 and c == C:
            ans += 1
        return
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if m[nr][nc] == '.':
            m[nr][nc] = 'X'
            go(nr, nc, d+1)
            m[nr][nc] = '.'

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]
ans = 0
m[R][1] = 'X'
go(R, 1, 1)
print(ans)