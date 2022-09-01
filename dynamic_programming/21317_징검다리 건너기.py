# https://www.acmicpc.net/problem/21317
import sys

def fill(least, beg):
    for i in range(beg, N):
        least[i] = min(least[i-1] + energy[i-1][0], least[i-2] + energy[i-2][1])

N = int(sys.stdin.readline())
energy = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
k = int(sys.stdin.readline())

if N == 1:
    print(0)
elif N == 2:
    print(energy[0][0])
else:
    least = [0 for _ in range(N)]
    least[1] = energy[0][0]
    fill(least, 2)
    ans = least[-1]

    for i in range(N-1, 2, -1):
        bbj = least[i-3] + k
        if bbj < least[i]:
            least[i] = bbj
            fill(least, i+1)
            ans = min(ans, least[-1])
    print(ans)