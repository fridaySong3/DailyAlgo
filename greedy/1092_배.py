# https://www.acmicpc.net/problem/1092
import sys
C = int(sys.stdin.readline())
crane = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
B = int(sys.stdin.readline())
box = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

if box[0] > crane[0]:
    print(-1)
    exit()

canMovIdx = [-1] * C
c, b = 0, 0
while c < C and b < B:
    if box[b] <= crane[c]:
        canMovIdx[c] = b
        c += 1
    else:
        b += 1

t = 0
while True:
    for c in range(C):
        if canMovIdx[c] == -1:
            continue
        moveSth = False
        for i in range(canMovIdx[c], B):
            if box[i] != -1:
                box[i] = -1
                canMovIdx[c] = i + 1
                moveSth = True
                break
        if not moveSth:
            canMovIdx[c] = -1
    if sum([1 for i in canMovIdx if i == -1]) == C:
        break
    t += 1
print(t)