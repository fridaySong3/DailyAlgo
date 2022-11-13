# https://www.acmicpc.net/problem/1337
import sys
NUM = 5
N = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(N)])
same_group = 1
j = 1
sg = 1
for i in range(N):
    end = arr[i] + NUM
    while j < N and arr[j] < end:
            sg += 1
            j += 1
    if sg > same_group:
        same_group = sg
    sg -= 1
print(NUM - same_group)