# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque 

def dfs(idx, computers, visit):
    visit[idx] = True
    for i in range(len(visit)):
        if computers[idx][i] == 1 and idx != i and not visit[i]:
            dfs(i, computers, visit)

def bfs(start, computers, visit):
    q = deque([start])
    while len(q) > 0:
        idx = q.popleft()
        if visit[idx] == True:
            continue
        visit[idx] = True
        for i in range(len(visit)):
            if computers[idx][i] == True and idx != i and not visit[i]:
                q.append(i)
                
def solution(n, computers):
    answer = 0
    
    visit = [False for _ in range(n)]
    for i in range(n):
        if not visit[i]:
            dfs(i, computers, visit)
            # bfs(i, computers, visit)
            answer += 1
    
    return answer