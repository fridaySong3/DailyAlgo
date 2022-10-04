# https://www.acmicpc.net/problem/1052
import sys
N, K = map(int, sys.stdin.readline().split())
initN = N
while True:
    binN = bin(N)[2:]
    if bin(N).count('1') <= K:
        break
    exp = len(binN) - binN.rfind('1') - 1
    N += 1 << exp
print(N - initN)