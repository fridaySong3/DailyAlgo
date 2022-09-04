# https://www.acmicpc.net/problem/16198
N = int(input())
Ws = list(map(int, input().split()))
def bruteforce(weights, energy):
    global ans
    if len(weights) == 2:
        ans = max(ans, energy)
    for i in range(1, len(weights)-1):
        e = energy + weights[i-1] * weights[i+1]
        bruteforce(weights[:i] + weights[i+1:], e)

ans = 0
bruteforce(Ws, 0)
print(ans)