# https://www.acmicpc.net/problem/11256
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    J, N = map(int, sys.stdin.readline().split())
    boxSize = []
    for _ in range(N):
        r, c = map(int, sys.stdin.readline().split())
        boxSize.append(r * c)
    boxSize.sort(reverse=True)
    acc = 0
    for i in range(N):
        acc += boxSize[i]
        if acc >= J:
            print(i + 1)
            break