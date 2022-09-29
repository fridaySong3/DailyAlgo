# https://www.acmicpc.net/problem/15886
import sys
N = int(sys.stdin.readline())
route = sys.stdin.readline().rstrip()
new_route = []
i = 0
while i < N-1:
    if route[i] != route[i+1]:
        new_route.append(route[i])
    i += 1
new_route.append(route[-1])
if len(new_route) % 2 == 0:
    if new_route[0] == 'E':
        print(len(new_route) // 2)
    else:
        print(len(new_route) // 2 + 1)
else:
    print((len(new_route) + 1) // 2)