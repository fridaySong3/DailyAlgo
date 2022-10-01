# https://www.acmicpc.net/problem/2232
import sys

explode_num = 0
def explode(power, dir):
    global explode_num, bomb
    for j in dir:
        if 0 < bomb[j] < power:
            power = bomb[j]
            bomb[j] = 0
            explode_num += 1
        else:
            break

N = int(sys.stdin.readline())
bomb = [int(sys.stdin.readline()) for _ in range(N)]
si = sorted(range(N), key=lambda x: bomb[x], reverse=True)
answer = []
for i in si:
    if bomb[i] == 0:
        continue
    answer.append(i+1)
    explode_num += 1
    explode(bomb[i], range(i-1, -1, -1))
    explode(bomb[i], range(i+1, N))
    bomb[i] = 0
    if explode_num == N:
        break
for i in sorted(answer):
    print(i)
    