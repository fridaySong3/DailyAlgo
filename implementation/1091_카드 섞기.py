# https://www.acmicpc.net/problem/1091
import sys

def isValid(cards, P):
    for idx, card in enumerate(cards):
        desirable = P[card]
        real = idx % 3
        if desirable != real:
            return False
    return True

def shuffle(cards, S):
    tmp = [0] * len(cards)
    for order, seat in enumerate(S):
        tmp[seat] = cards[order]
    return tuple(tmp)
    
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
S = list(map(int, sys.stdin.readline().split()))

init = tuple(range(N))
cards = init
shNum = 0
while not isValid(cards, P):
    cards = shuffle(cards, S)
    shNum += 1
    if cards == init:
        shNum = -1
        break
print(shNum)