# https://www.acmicpc.net/problem/20186
import sys
N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort(reverse=True)
print(sum(nums[:K]) - (K * (K - 1) // 2))