# https://www.acmicpc.net/problem/9237
import sys
N = int(sys.stdin.readline())
days = list(map(int, sys.stdin.readline().split()))
days.sort(reverse=True)
print(max([i + d + 1 for i, d in enumerate(days)]) + 1)