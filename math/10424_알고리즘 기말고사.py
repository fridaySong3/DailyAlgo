# https://www.acmicpc.net/problem/10424
import sys
N = int(sys.stdin.readline())
answer = [0] * N
rank = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    answer[rank[i]-1] = rank[i] - (i+1)
for a in answer:
    print(a)