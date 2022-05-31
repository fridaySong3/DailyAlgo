import sys
from collections import deque

C, R, H = map(int, sys.stdin.readline().split())
box = [[[None for _ in range(C+2)] for _ in range(R+2)] for _ in range(H+2)]
for h in range(1, H+1):
    for r in range(1, R+1):
        box[h][r][1:C+1] = map(int, sys.stdin.readline().split())

queue = deque()
for h in range(1, H+1):
    for r in range(1, R+1):
        for c in range(1, C+1):
            if box[h][r][c] == 1:
                queue.append((h, r, c))

dhs = [1, -1, 0, 0, 0, 0]
drs = [0, 0, 1, -1, 0, 0]
dcs = [0, 0, 0, 0, 1, -1]

visit = [[[False for _ in range(C+2)] for _ in range(R+2)] for _ in range(H+2)]    
date = 1
while queue:
    h, r, c = queue.popleft()
    if visit[h][r][c]:
        continue
    visit[h][r][c] = True
    
    for dh, dr, dc in zip(dhs, drs, dcs):
        nh, nr, nc = h + dh, r + dr, c + dc
        if box[nh][nr][nc] == 0:
            box[nh][nr][nc] = box[h][r][c] + 1
            date = box[nh][nr][nc]
            queue.append((nh, nr, nc))

find_zero = False
for h in range(1, H+1):
    for r in range(1, R+1):
        for c in range(1, C+1):
            if box[h][r][c] == 0:
                find_zero = True
                break
if find_zero:
    print(-1)
else:
    print(date - 1)