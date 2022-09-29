# https://www.acmicpc.net/problem/10157
R, C = map(int, input().split())
k = int(input())
max_k = R * C

if k > max_k:
    print(0)
else:
    seats = [[0] * C for _ in range(R)]
    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
    d = 0
    r, c = 0, 0
    for i in range(1, k):
        seats[r][c] = i
        nr, nc = r + dir[d][0], c + dir[d][1]
        if 0 <= nr < R and 0 <= nc < C and seats[nr][nc] == 0:
            r, c = nr, nc
        else:
            d = (d + 1) % len(dir)
            r, c = r + dir[d][0], c + dir[d][1]
    print(r+1, c+1)