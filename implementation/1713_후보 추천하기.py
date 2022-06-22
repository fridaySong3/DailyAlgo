# https://www.acmicpc.net/problem/1713
import sys

def outdated(c, c_out):
    return c[1] < c_out[1] or (c[1] == c_out[1] and c[2] < c_out[2])

N = int(sys.stdin.readline())
R = int(sys.stdin.readline())
recommend = list(map(int, sys.stdin.readline().split()))

candidates = [] # [후보번호, 추천수, 첫추천순서]
for r in range(R):
    idx = -1
    for c in range(len(candidates)):
        if recommend[r] == candidates[c][0]:
            idx = c
            break
    if idx != -1:
        candidates[idx][1] += 1
    else:
        if len(candidates) < N:
            candidates.append([recommend[r], 0, r])
        else:
            out = 0
            for c in range(1, len(candidates)):
                if outdated(candidates[c], candidates[out]):
                    out = c
            candidates[out] = [recommend[r], 0, r]

candidates.sort()
for c in candidates:
    print(c[0], end=" ")