# https://www.acmicpc.net/problem/14728
import sys

answer = 0

def promising(idx, left, score):
    for i in range(idx, len(ks)):
        if left >= ks[i][0]:
            score += ks[i][1]
            left -= ks[i][0]
        elif left == 0:
            break
        else:
            score += ks[i][1] / (ks[i][0] / left)
            break
    return score > answer

def backtracking(idx, left, score):
    if idx >= len(ks):
        return score
    new_left = left - ks[idx][0]
    new_score = score + ks[idx][1]
    global answer
    if new_left >= 0 and promising(idx + 1, new_left, new_score):
        answer = max(answer, backtracking(idx + 1, new_left, new_score))
    if promising(idx + 1, left, score):
        answer = max(answer, backtracking(idx + 1, left, score))
    return answer

N, T = map(int, sys.stdin.readline().split())
ks = [0 for _ in range(N)]
for i in range(N):
    k, s = map(int, sys.stdin.readline().split())
    ks[i] = (k, s)

ks.sort(key=lambda x: x[1]/x[0], reverse=True)

backtracking(0, T, 0)
print(answer)