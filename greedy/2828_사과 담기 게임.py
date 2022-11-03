# https://www.acmicpc.net/problem/2828
import sys

N, M = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())
apple_loc = [int(sys.stdin.readline()) for _ in range(J)]

front, back = 1, M
ans = 0

for loc in apple_loc:
    if front <= loc <= back:
        continue
    elif loc < front:
        mov = front - loc
        ans += mov
        front = loc
        back -= mov
    else: # back < loc
        mov = loc - back
        ans += mov
        front += mov
        back = loc
        
print(ans)