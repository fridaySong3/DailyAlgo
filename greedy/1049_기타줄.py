# https://www.acmicpc.net/problem/1049
import sys
bundleNum = 6
N, M = map(int, sys.stdin.readline().split())
bundleMin = 1000
oneMin = 1000
for _ in range(M):
    b, o = map(int, sys.stdin.readline().split())
    bundleMin = min(bundleMin, b)
    oneMin = min(oneMin, o)
if (bundleMin / bundleNum) < oneMin:
    q, r = divmod(N, bundleNum)
    print(min(q * bundleMin + r * oneMin, (q+1) * bundleMin))
else:
    print(N * oneMin)