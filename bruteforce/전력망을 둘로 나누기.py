# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def count_node(start, adj): # bfs
    visit = set()
    q = deque([start])
    while q:
        n = q.popleft()
        if n in visit:
            continue
        visit.add(n)
        for nn in adj[n]:
            if nn not in visit:
                q.append(nn)
    return len(visit)

def solution(n, wires):
    answer = 100
    
    # make adjacent list
    adj = dict()
    for i in range(1, n+1):
        adj[i] = set()
    
    for n1, n2 in wires:
        adj[n1].add(n2)
        adj[n2].add(n1)
    
    # process
    for n1, n2 in wires:
        adj[n1].remove(n2)
        adj[n2].remove(n1)
        
        cnt = count_node(1, adj)
        answer = min(answer, abs((n - cnt) - cnt))
        
        adj[n1].add(n2)
        adj[n2].add(n1)
        
    return answer