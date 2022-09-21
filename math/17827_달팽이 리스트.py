# https://www.acmicpc.net/problem/17827
import sys
N, M, V = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
V_idx = V - 1
cycle_len = N - V_idx
for _ in range(M):
    step = int(sys.stdin.readline())
    if step < N:
        print(arr[step])
    else:
        print(arr[(step-N) % cycle_len + V_idx])