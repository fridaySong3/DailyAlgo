# https://www.acmicpc.net/problem/11068
import sys


def transport(b, n):
    result = []
    while n >= b:
        result.append(n % b)
        n = n // b
    result.append(n)
    return result


def is_palin(l):
    i = 0
    half = len(l) // 2
    while i < half:
        j = len(l) - (i+1)
        if l[i] != l[j]:
            return False
        i += 1
    return True


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    success = False
    for b in range(2, 65):
        if is_palin(transport(b, N)):
            success = True
            break
    if success:
        print(1)
    else:
        print(0)
