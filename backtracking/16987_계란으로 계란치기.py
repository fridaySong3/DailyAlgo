# https://www.acmicpc.net/problem/16987
import sys
N = int(sys.stdin.readline())
egg = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def damage(a, b):
    egg[a][0] = egg[a][0] - egg[b][1]
    return 0 if egg[a][0] > 0 else 1

def recover(a, b):
    egg[a][0] = egg[a][0] + egg[b][1]
        
def bruteforce(idx, broken):
    global ans
    if broken == N or broken == N-1 or idx == N:
        ans = max(ans, broken)
        return
    if (N - idx) * 2 + broken <= ans: # is promising
        return
    if egg[idx][0] <= 0:
        bruteforce(idx+1, broken)
        return
    for i in range(N):
        if i != idx and egg[i][0] > 0:
            bruteforce(idx+1, broken + damage(idx, i) + damage(i, idx))
            recover(idx, i)
            recover(i, idx)

ans = 0
bruteforce(0, 0)
print(ans)