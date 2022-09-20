# https://www.acmicpc.net/problem/1080
import sys

def op(arr, x, y):
    for nx in range(x, x+3):
        for ny in range(y, y+3):
            arr[nx][ny] = not arr[nx][ny]

N, M = map(int, sys.stdin.readline().split())
mat1 = [sys.stdin.readline().rstrip() for _ in range(N)]
mat2 = [sys.stdin.readline().rstrip() for _ in range(N)]
diff = [[False]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if mat1[r][c] != mat2[r][c]:
            diff[r][c] = True
ans = 0
for r in range(N):
    for c in range(M):
        if diff[r][c]:
            if r <= N - 3 and c <= M - 3:
                ans += 1
                op(diff, r, c)
            else:
                ans = -1
                break
    if ans == -1:
        break
print(ans)