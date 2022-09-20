# https://www.acmicpc.net/problem/11399
import sys
from itertools import accumulate
N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
print(sum(accumulate(sorted(times))))