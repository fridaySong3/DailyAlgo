# https://www.acmicpc.net/problem/11509
import sys

MAX_H = 1000000

N = int(sys.stdin.readline())
height = map(int, sys.stdin.readline().split())
left = [0 for _ in range(MAX_H+2)]
answer = 0
for h in height:
    if left[h+1] > 0:
        left[h+1] -= 1
    else:
        answer += 1
    left[h] += 1
print(answer)