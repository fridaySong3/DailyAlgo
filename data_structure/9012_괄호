# https://www.acmicpc.net/problem/9012
import sys

N = int(sys.stdin.readline())
for _ in range(N):
    line = sys.stdin.readline().rstrip()
    st = 0
    good = True
    for ch in line:
        if ch == '(':
            st += 1
        else:
            if st > 0:
                st -= 1
            else:
                good = False
                break
    if good and st == 0:
        print("YES")
    else:
        print("NO")
        