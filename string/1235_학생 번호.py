# https://www.acmicpc.net/problem/1235
import sys

def same_num(s1, s2):
    i = 0
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            i += 1
        else:
            break
    return i

N = int(sys.stdin.readline())
nums = [None for _ in range(N)]
for i in range(N):
    nums[i] = sys.stdin.readline().strip()
    nums[i] = nums[i][::-1]

nums.sort()
k = 0
for i in range(N-1):
    k = max(k, same_num(nums[i], nums[i+1]))

print(k+1)