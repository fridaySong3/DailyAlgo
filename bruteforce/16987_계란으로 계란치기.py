# https://www.acmicpc.net/problem/16987
import sys
N = int(sys.stdin.readline())
egg = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def damage(a, b):
    egg[a][0] = egg[a][0] - egg[b][1]
    if egg[a][0] <= 0:
        broken[a] = True

def recover(a, b):
    egg[a][0] = egg[a][0] + egg[b][1]
    if egg[a][0] > 0:
        broken[a] = False
        
def bruteforce(idx):
    global ans
    broken_num = broken.count(True)
    if broken_num == N or broken_num == N-1 or idx == N:
        ans = max(ans, broken_num)
        return
    if broken[idx]:
        bruteforce(idx+1)
        return
    for i in range(N):
        if i != idx and not broken[i]:
            damage(idx, i)
            damage(i, idx)
            bruteforce(idx+1)
            recover(idx, i)
            recover(i, idx)

ans = 0
broken = [False] * N
bruteforce(0)
print(ans)