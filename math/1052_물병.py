# https://www.acmicpc.net/problem/1052
import sys

# 가장 물이 적게 담긴 물병 두 개를 합치고, 이때 얼마만큼의 물병을 구매했는지 반환
def merge(eq):
    s = eq.pop() 
    b = eq.pop()
    added = (1 << b) - (1 << s) # 추가된 물병 개수
    # 합쳐진 물병이 기존 물병과 합쳐질 수 있다면 최대한 합침
    while len(eq) > 0 and eq[-1] == (b + 1):
        b = eq.pop()
    eq.append(b + 1)
    return added

N, K = map(int, sys.stdin.readline().split())
if N <= K:
    print(0)
else:
    eq = [] # N을 2의 거듭제곱의 합으로 나타내었을 때, 그 지수들을 내림차순으로 저장
    while N > 0:
        i = 0
        while N >= (1 << i):
            i += 1
        i -= 1
        eq.append(i)
        N -= (1 << i)
        
    # 물병의 개수가 K개 이하가 될 때까지 물병을 구매하여 합침
    added = 0
    while len(eq) > K:
        added += merge(eq)
    print(added)
    