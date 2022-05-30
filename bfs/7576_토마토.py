# https://www.acmicpc.net/problem/7576
import sys
from collections import deque

# 입력
C, R = map(int, sys.stdin.readline().split())
box = [[None for _ in range(C+2)] for _ in range(R+2)]
for nr in range(1, R+1):
    box[nr][1:C+1] = list(map(int, sys.stdin.readline().split()))

# 초기에 익은 토마토 queue에 넣기
q = deque()
for r in range(1, R+1):
    for c in range(1, C+1):
        if box[r][c] == 1:
            q.append((r, c))

# bfs
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
date = 1
visit = [[False for _ in range(C+2)] for _ in range(R+2)]
while q:
    n = q.popleft()
    r, c = n
    if visit[r][c]:
        continue
    visit[r][c] = True
    for x, y in zip(dx, dy):
        nr = r + x
        nc = c + y
        if box[nr][nc] == 0:
            box[nr][nc] = box[r][c] + 1
            date = box[nr][nc]
            q.append((nr, nc))

# 모두 익었는지 확인
all_matured = True
for r in range(1, R+1):
    if 0 in box[r]:
        all_matured = False
        break

# 출력
print(date-1) if all_matured else print(-1)