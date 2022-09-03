# https://www.acmicpc.net/problem/2992
X = list(input().rstrip())
found = False
for i in range(len(X)-1, 0, -1):
    if X[i-1] < X[i]:
        for j in range(len(X)-1, 0, -1):
            if X[i-1] < X[j]:
                X[i-1], X[j] = X[j], X[i-1]
                X = X[:i] + list(reversed(X[i:]))
                break
        print(''.join(X))
        found = True
        break
if not found:
    print(0)