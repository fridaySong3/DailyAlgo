# https://www.acmicpc.net/problem/5014

import sys

F, S, G, U, D = map(int, sys.stdin.readline().split())

visit = [False for _ in range(F+1)]
here = S
move = 0

while True:
    if not (1 <= here <= F):
        print("use the stairs")
        break
    
    if visit[here]:
        print("use the stairs")
        break
    visit[here] = True
    
    if here == G:
        print(move)
        break
    
    if (here < G and here + U > F) or (here > G and here - D >= 1):
        here -= D
    else:
        here += U
    
    move += 1