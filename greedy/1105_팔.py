# https://www.acmicpc.net/problem/1105
import sys

def get_len(num):
    return len(str(num))

def digit(num, k):
    return num // (10**k) % 10

L, R = map(int, sys.stdin.readline().split())

k = get_len(R) - 1
answer = 0
while k >= 0 and digit(R, k) == digit(L, k):
    if digit(R, k) == 8:
        answer += 1
    k -= 1

print(answer)