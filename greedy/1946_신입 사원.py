# https://www.acmicpc.net/problem/1946
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    scores = [0] * (N+1)
    for _ in range(N):
        s1, s2 = map(int, sys.stdin.readline().split())
        scores[s1] = s2
    ans = 1
    prev_s = scores[1]
    for i in range(2, len(scores)):
        s = scores[i]
        if s < prev_s:
            ans += 1
            prev_s = s
        
    print(ans)