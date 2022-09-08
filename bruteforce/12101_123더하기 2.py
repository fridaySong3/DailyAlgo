# https://www.acmicpc.net/problem/12101
N, K = map(int, input().split())

def bruteforce(eq, s):
    if s == N:
        ans.append('+'.join(eq))
    for i in range(1, 4):
        if s + i <= N:
            eq.append(str(i))
            bruteforce(eq, s+i)
            eq.pop()
ans = []    
bruteforce([], 0)
if len(ans) < K:
    print(-1)
else:
    ans.sort()
    print(ans[K-1])