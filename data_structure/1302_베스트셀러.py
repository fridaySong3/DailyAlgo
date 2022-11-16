# https://www.acmicpc.net/problem/1302
import sys
from collections import Counter
N = int(sys.stdin.readline())
selled = sorted([sys.stdin.readline().rstrip() for _ in range(N)])
selled = Counter(selled).most_common()
print(selled[0][0])
