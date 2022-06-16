# https://www.acmicpc.net/problem/1021
import sys
from collections import deque

def in_range(front, r, removed):
    cnt = 0
    if front < r:
        for rd in removed:
            if front < rd < r:
                cnt += 1
    elif front > r:
        for rd in removed:
            if front < rd or rd < r:
                cnt += 1
    else:
        return 0
    return cnt

N, M = map(int, sys.stdin.readline().split())
remove = list(map(int, sys.stdin.readline().split()))

q= deque([i for i in range(1, N+1)])
answer = 0
for i in range(len(remove)):
    front = q.popleft()
    ffront = front - N if front > remove[i] else front
    q.appendleft(front)
    left = remove[i] - ffront - in_range(front, remove[i], remove[:i])
    right = len(q) - left
    if left < right:
        q.rotate(-left)
        answer += left
    else:
        q.rotate(right)
        answer += right
    q.popleft()
print(answer)