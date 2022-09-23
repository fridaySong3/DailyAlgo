# https://www.acmicpc.net/problem/17472
# Kruskal 참조) https://deeppago.tistory.com/m/31
import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N, M = map(int, sys.stdin.readline().split())
gido = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
moseori = []

def next(r, c, dir):
    global dr, dc
    return r + dr[dir], c + dc[dir]

def bfs(que: deque, sn: int):
    global gido, moseori, dr, dc
    while que:
        r, c = que.popleft()
        if gido[r][c] != 1:
            continue
        gido[r][c] = sn
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < len(gido) and 0 <= nc < len(gido[0]):
                if gido[nr][nc] == 0:
                    moseori.append((r, c, i, sn))
                elif gido[nr][nc] == 1:
                    que.append((nr, nc))

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
sNum = 2
for i in range(N):
    for j in range(M):
        if gido[i][j] == 1:
            bfs(deque([(i, j)]), sNum)
            sNum += 1
edges = set()
for r, c, dir, sn in moseori:
    length = 0
    while True:
        r, c = next(r, c, dir)
        if not(0 <= r < len(gido) and 0 <= c < len(gido[0])):
            break
        if gido[r][c] != 0:
            if sn < gido[r][c] and length >= 2:
                edges.add((length, sn, gido[r][c]))
            break
        length += 1
edges = list(edges)
edges.sort()
parent = [0] * (sNum)
for i in range(2, sNum):
    parent[i] = i

result = 0
edgeNum = 0
# 정렬된 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은것이므로  
    if find_parent(parent, a) != find_parent(parent, b):
        # 신장 트리에 간선 추가
        union_parent(parent, a, b)
        result += cost
        edgeNum += 1

vNum = sNum - 2
if edgeNum < vNum-1:
    print(-1)
else:
    print(result)