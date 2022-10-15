# https://www.acmicpc.net/problem/1158
from collections import deque

N, K = map(int, input().split())
q = deque(range(1, N+1))
ans = []
while q:
    for i in range(K-1):
        num = q.popleft()
        q.append(num)
    ans.append(str(q.popleft()))
print("<", ", ".join(ans), ">", sep="")