# https://www.acmicpc.net/problem/14888
import sys
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divi(a, b):
    if a < 0:
        return -((-a) // b)
    return a // b

def bruteforce(ni, result):
    global maxi, mini
    if sum(op_num) == 0:
        maxi = max(maxi, result)
        mini = min(mini, result)
    for i in range(4):
        if op_num[i] > 0:
            op_num[i] -= 1
            bruteforce(ni+1, op[i](result, nums[ni]))
            op_num[i] += 1

N = int(sys.stdin.readline())
nums = N = list(map(int, sys.stdin.readline().split()))
op_num = list(map(int, sys.stdin.readline().split()))
op = [add, sub, mul, divi]

maxi = -(10**9)
mini = 10**9
bruteforce(1, nums[0])
print(maxi)
print(mini)