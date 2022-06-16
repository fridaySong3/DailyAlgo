# https://www.acmicpc.net/problem/2573
# 구현, dfs/bfs 
import sys

class Info:
    def __init__(self, num, neighbor):
        self.num = num # 자신의 빙하 수치
        self.neighbor = neighbor # 빙하가 다 녹지 않은 이웃 빙하의 좌표(r, c) 컬렉션

def get_neighbor(arr, r, c):
    s = set()
    diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i, j in diff:
        if arr[r+i][c+j] != 0:
            s.add((r+i, c+j))
    return s

def is_connected(graph):
    visit = set()
    queue = [list(graph.keys())[0]]
    
    # bfs
    while len(queue) != 0:
        key = queue[0]
        if key in visit:
            del queue[0]
            continue
        visit.add(key)
        for neighbor_key in graph[key].neighbor:
            if not neighbor_key in visit:
                queue.append(neighbor_key)
        del queue[0]
        
    return True if len(visit) == len(graph) else False

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append( list(map(int, sys.stdin.readline().split())) )

graph = dict()
for r in range(1, N-1):
    for c in range(1, M-1):
        if arr[r][c] != 0:
            graph[(r,c)] = Info(arr[r][c], get_neighbor(arr, r, c))

year = 0
while len(graph) != 0:
    year += 1
    
    # melting
    melt = []
    for key in list(graph.keys()):
        graph[key].num -= 4 - len(graph[key].neighbor)
        if graph[key].num <= 0:
            melt.append(key)
    
    # update graph
    for key in melt:
        for nei_key in graph[key].neighbor:
            graph[nei_key].neighbor.remove(key)
        del graph[key]
    
    if len(graph) == 0: # 빙산이 모두 녹음
        break
    if len(melt)!=0 and not is_connected(graph): # 빙산이 녹아서 쪼개짐
        break
            
print(year if len(graph) != 0 else 0)