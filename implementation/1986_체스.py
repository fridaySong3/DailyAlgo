# acmicpc.net/problem/1986
import sys

def minus_one(a):
    return a - 1

N, M = map(int, sys.stdin.readline().split())
_, *qloc = list(map(minus_one, map(int, sys.stdin.readline().split())))
_, *kloc = list(map(minus_one, map(int, sys.stdin.readline().split())))
_, *ploc = list(map(minus_one, map(int, sys.stdin.readline().split())))

dk = ((-2,-1), (-2,+1), (-1,-2), (-1,+2), (+2,-1), (+2,+1), (+1,-2), (+1,+2))
dq = ((+1, 0), (-1, 0), (0, +1), (0, -1), (-1,-1), (-1,+1), (+1,+1), (+1,-1))

board = [[0] * M for _ in range(N)]

for i in range(0, len(kloc), 2):
    r, c = kloc[i], kloc[i+1]
    board[r][c] = 1

for i in range(0, len(ploc), 2):
    r, c = ploc[i], ploc[i+1]
    board[r][c] = 1

for i in range(0, len(qloc), 2):
    r, c = qloc[i], qloc[i+1]
    board[r][c] = 1
    for dr, dc in dq:
        nr, nc = r + dr, c + dc
        while 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 1:
            board[nr][nc] = 2
            nr, nc = nr + dr, nc + dc
    
for i in range(0, len(kloc), 2):
    r, c = kloc[i], kloc[i+1]
    for dr, dc in dk:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            board[nr][nc] = 2

answer = 0
for b in board:
    answer += b.count(0)
print(answer)