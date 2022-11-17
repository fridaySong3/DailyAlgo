# https://www.acmicpc.net/problem/1253
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

cnt_n = dict() # cnt_n[num] = set([indice of num])
for i in range(N):
    if nums[i] not in cnt_n:
        cnt_n[nums[i]] = set([i])
    else:
        cnt_n[nums[i]].add(i)
        
ans = 0
for i in range(N):
    for j in range(i+1, N):
        comb = (i, j)
        s = nums[i] + nums[j]
        if s in cnt_n and len(cnt_n[s]) > 0:
            exist = set([k for k in comb if k in cnt_n[s]])
            ans += len(cnt_n[s]) - len(exist)
            cnt_n[s] = exist
print(ans)