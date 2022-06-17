# https://www.acmicpc.net/problem/1026
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

answer = 0
for a, b in zip(A, B):
    answer += a * b
print(answer)