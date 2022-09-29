# https://www.acmicpc.net/problem/1374
import sys
N = int(sys.stdin.readline())
lessons = []
for _ in range(N):
    _, s, e = map(int, sys.stdin.readline().split())
    lessons.append((s, 1))
    lessons.append((e, -1))
lessons.sort()
answer = 0
overlap = 0
for _, d in lessons:
    overlap += d
    answer = max(answer, overlap)
print(answer)
