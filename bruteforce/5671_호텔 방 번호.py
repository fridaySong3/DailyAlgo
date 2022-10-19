# https://www.acmicpc.net/problem/5671
import sys
while True:
    try:
        N, M = map(int, sys.stdin.readline().split())
    except:
        break
    else:
        ans = 0
        for i in range(N, M+1):
            si = str(i)
            if len(si) == len(set(si)):
                ans += 1
        print(ans)