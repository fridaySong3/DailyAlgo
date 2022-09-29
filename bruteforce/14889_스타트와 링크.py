# https://www.acmicpc.net/problem/14889
import sys

def to_bin(comb):
    ans = 0
    for c in comb:
        ans |= 1 << c
    return ans

def dfs(idx, include, s):
    global S, H, sum_s
    if len(include) == H:
        sum_s[to_bin(include)] = s
        return
    if len(include) + N - idx < H:
        return
    
    dfs(idx+1, include, s)
    
    for i in include:
        s += S[i][idx]
        s += S[idx][i]
    include.append(idx)
    dfs(idx+1, include, s)
    include.pop()
    
N = int(sys.stdin.readline())
S = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
H = N // 2
sum_s = dict()
dfs(0, [], 0)
num = (1 << N) - 1
ans = float('inf')
for key in sum_s:
    ans = min(ans, abs(sum_s[num ^ key] - sum_s[key]))
print(ans)