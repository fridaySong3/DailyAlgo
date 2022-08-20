# https://www.acmicpc.net/problem/4108
import sys
while True:
    R, C = map(int, sys.stdin.readline().split())
    if R == 0 and C == 0:
        break
    m = [[None for _ in range(C+2)] for _ in range(R+2)]
    for r in range(1, len(m)-1):
        m[r][1:-1] = list(sys.stdin.readline())[:-1]
    
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    ans = []
    for r in range(1, len(m)-1):
        line = []
        for c in range(1, len(m[r])-1):
            if m[r][c] == '*':
                line.append('*')
            else:
                sum = 0
                for x, y in zip(dx, dy):
                    if m[r+x][c+y] == '*':
                        sum += 1
                line.append(str(sum))
        ans.append(''.join(line))
    print('\n'.join(ans))