# https://www.acmicpc.net/problem/2780
import sys

T = int(sys.stdin.readline())
N = [int(sys.stdin.readline()) for _ in range(T)]

adjust = [
    [7],
    [2, 4],
    [1, 3, 5],
    [2, 6],
    [1, 5, 7],
    [2, 4, 6, 8],
    [3, 5, 9],
    [4, 8, 0],
    [7, 5, 9],
    [6, 8]
]
nums = 10
cnt = [[1 for _ in range(nums)] for _ in range(max(N)+1)]
for r in range(2, len(cnt)):
    for c in range(nums):
        cnt[r][c] = sum([cnt[r-1][adj] for adj in adjust[c]])

for n in N:
    print(sum(cnt[n]) % 1234567)