# https://www.acmicpc.net/problem/1063
import sys
SIZE = 8

def to_coordinate(loc):
    r = SIZE - int(loc[1])
    c = ord(loc[0]) - ord('A')
    return r, c

def to_str(r, c):
    return chr(c + ord('A')) + str(SIZE - r)

dir = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RB': (1, 1),
    'LB': (1, -1),
    'RT': (-1, 1),
    'LT': (-1, -1),
}
king, stone, N = sys.stdin.readline().split()
kx, ky = to_coordinate(king)
sx, sy = to_coordinate(stone)
for _ in range(int(N)):
    dx, dy = dir[sys.stdin.readline().rstrip()]
    nkx, nky = kx + dx, ky + dy
    if not (0 <= nkx < SIZE and 0 <= nky < SIZE):
        continue
    if sx == nkx and sy == nky:
        nsx, nsy = sx + dx, sy + dy
        if not (0 <= nsx < SIZE and 0 <= nsy < SIZE):
            continue
        sx, sy = nsx, nsy
    kx, ky = nkx, nky
print(to_str(kx, ky))
print(to_str(sx, sy))