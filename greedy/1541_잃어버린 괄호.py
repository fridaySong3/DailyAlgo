# https://www.acmicpc.net/problem/1541
import sys
eqs = sys.stdin.readline().split("-")
nums = []
for eq in eqs:
    nums.append(sum(map(int, eq.split("+"))))

print(nums[0] - sum(nums[1:]))