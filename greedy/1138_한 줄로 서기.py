# https://www.acmicpc.net/problem/1138
N = int(input())
order = [0] * N
for pn, tallNum in enumerate(map(int, input().split())):
    cntEmpty = 0
    for i in range(N):
        if order[i] == 0:
            cntEmpty += 1
        if cntEmpty == tallNum + 1:
            break
    order[i] = pn + 1
print(' '.join(map(str, order)))