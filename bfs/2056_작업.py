# https://www.acmicpc.net/problem/2056
import sys
from collections import deque

N = int(sys.stdin.readline())
time = [0 for _ in range(N+1)]
prev = [[] for _ in range(N+1)]
post = [[] for _ in range(N+1)]

for i in range(1, N+1):
    info = list(map(int, sys.stdin.readline().split()))
    time[i] = info[0]
    if info[1] > 0:
        prev[i] = info[2:]
        for j in prev[i]:
            post[j].append(i)

# print(time, prev, post)

q = deque()
for i in range(1, len(post)):
    if len(post[i]) == 0:
        q.append(i)

max_t = [None for _ in range(N+1)]
while len(q) != 0:
    job = q.popleft()
    if max_t[job] != None: # if visit
        continue
    
    if len(post[job]) == 0:
        max_t[job] = time[job]
    elif all( [max_t[pj] != None for pj in post[job]] ):
        max_t[job] = time[job] + max([max_t[pj] for pj in post[job]])
    else: # too early to visit
        continue
    q.extend(prev[job])
    
print(max(max_t[1:]))