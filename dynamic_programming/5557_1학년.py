# https://www.acmicpc.net/problem/5557
import sys

M, m = 20, 0

def dfs(idx, acc):
    global M, m, dp
    
    if idx == len(eq):
        if acc == result:
            return 1
        return 0
    
    if dp[idx][acc] != None:
        return dp[idx][acc]
    
    n1, n2 = 0, 0
    acc_p = acc + eq[idx]
    if m <= acc_p <= M:
        n1 = dfs(idx+1, acc_p)
        
    acc_m = acc - eq[idx]
    if m <= acc_m <= M:
        n2 = dfs(idx+1, acc_m)
        
    dp[idx][acc] = n1 + n2
    return dp[idx][acc]

N = int(sys.stdin.readline())
*eq, result = map(int, sys.stdin.readline().split())
fornt_zero = (1 if eq[0] == 0 else 0)
eq = [e for e in eq if e != 0]
cnt_zero = N - 1 - len(eq)
zero_branch = 2**(cnt_zero - fornt_zero)

if len(eq) == 0:
    print(zero_branch)
else:
    dp = [[None] * (M+1) for _ in range(N)]
    answer = dfs(1, eq[0])
    print(answer * zero_branch)