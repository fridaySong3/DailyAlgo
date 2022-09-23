# https://www.acmicpc.net/problem/3190
import sys
from enum import IntEnum

APPLE = -2
DEFAULT = -1
N = int(sys.stdin.readline())
board = [[DEFAULT] * N for _ in range(N)]

K = int(sys.stdin.readline())
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    board[r-1][c-1] = APPLE
    
L = int(sys.stdin.readline())
td = []
for _ in range(L):
    time, dir = sys.stdin.readline().split()
    td.append((int(time), dir))

def print_board():
    global board
    print()
    for r in board:
        print(r)

class Dir(IntEnum):
    UP = 0, 
    RIGHT = 1, 
    DOWN = 2, 
    LEFT = 3
        
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
turnR = [Dir.RIGHT, Dir.DOWN, Dir.LEFT, Dir.UP]
turnL = [Dir.LEFT, Dir.UP, Dir.RIGHT, Dir.DOWN]
direct = [[0] * N for _ in range(N)]

sr, sc = 0, 0
er, ec = 0, 0
board[sr][sc] = 0
d = Dir.RIGHT
tdI = 0
while True:
    # print_board()
    if tdI < len(td) and board[sr][sc] == td[tdI][0]:
        if td[tdI][1] == 'D':
            d = turnR[d]
        else:
            d = turnL[d]
        tdI += 1
        
    direct[sr][sc] = d
    nextTime = board[sr][sc] + 1
    sr, sc = sr + dr[d], sc + dc[d]
    hitWall = not(0 <= sr < N and 0 <= sc < N)
    if hitWall: 
        print(nextTime)
        exit()
    hitBody = board[sr][sc] > DEFAULT
    if hitBody: 
        print(nextTime)
        exit()
    if board[sr][sc] != APPLE:
        board[er][ec] = DEFAULT
        er, ec = er + dr[direct[er][ec]], ec + dc[direct[er][ec]]
    board[sr][sc] = nextTime