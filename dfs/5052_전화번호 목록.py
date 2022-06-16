# https://www.acmicpc.net/problem/5052

import sys

def classify(nums, idx):
    if len(nums) < 2:
        return True
    classified = [[] for _ in range(10)]
    for num in nums:
        if idx >= len(num):
            return False
        classified[int(num[idx])].append(num)
    for i in range(len(classified)):
        is_valid = classify(classified[i], idx+1)
        if not is_valid:
            return False
    return True
    
T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    nums = []
    for _ in range(N):
        nums.append(sys.stdin.readline().strip())
    
    is_valid = classify(nums, 0)
    
    if is_valid:
        print("YES")
    else:
        print("NO")
