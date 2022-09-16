import sys
from itertools import combinations

N = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(sum(dice) - max(dice))
else:
    double = [d for d in list(combinations(range(6), 2)) if d not in [(0, 5), (1, 4), (2, 3)]]
    triple = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (5, 1, 2), (5, 1, 3), (5, 2, 4), (5, 3, 4)]

    max3 = min([dice[n1] + dice[n2] + dice[n3] for n1, n2, n3 in triple])
    max2 = min([dice[n1] + dice[n2] for n1, n2 in double])
    max1 = min(dice)

    num3 = 4
    num2 = 4 * (2 * N - 3)
    num1 = (N - 2) * (5 * N - 6)
    print((max3 * num3) + (max2 * num2) + (max1 * num1))