# https://www.acmicpc.net/problem/1931
import sys
N = int(sys.stdin.readline())
meeting = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0]))
ans = 0
prev_e = 0
for s, e in meeting:
    if s < prev_e:
        continue
    ans += 1
    prev_e = e
print(ans)