# https://www.acmicpc.net/problem/1263
import sys
N = int(sys.stdin.readline())
works = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)] # (time, due_time)
works.sort(key=lambda x: x[1], reverse=True) # sorting based due_time
post_work_start_time = works[0][1] - works[0][0]
for i in range(1, N):
    post_work_start_time = min(post_work_start_time, works[i][1]) - works[i][0]
if post_work_start_time < 0:
    print(-1)
else:
    print(post_work_start_time)
