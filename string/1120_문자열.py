# https://www.acmicpc.net/problem/1120
A, B = input().split()
ans = 50
for i in range(len(B) - len(A) + 1):
    ans = min(ans, sum([1 for a, b in zip(range(len(A)), range(i, i+len(A))) if A[a] != B[b]]))
print(ans)