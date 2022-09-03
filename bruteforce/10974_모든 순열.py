# https://www.acmicpc.net/problem/10974
N = int(input())
p = list(range(1, N+1))
rp = list(reversed(p))
while True:
    for n in p:
        print(n, end=' ')
    print()
    if p == rp:
        break
    for i in range(N-1, 0, -1):
        if p[i-1] < p[i]:
            for j in range(N-1, i-1, -1):
                if p[i-1] < p[j]:
                    p[i-1], p[j] = p[j], p[i-1]
                    break
            p = p[:i] + list(reversed(p[i:]))
            break
        