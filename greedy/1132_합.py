# https://www.acmicpc.net/problem/1132
import sys
M = 10
def idx(ch):
    return ord(ch) - ord('A')

N = int(sys.stdin.readline())
front = [False] * M
num = [0] * M
for _ in range(N):
    sn = sys.stdin.readline().rstrip()
    front[idx(sn[0])] = True
    for i in range(len(sn)):
        num[idx(sn[i])] += 10**(len(sn) - 1 - i)
sorted_num = sorted([(num[i], i) for i in range(M) if num[i] != 0])

if len(sorted_num) == M:
    for i in range(M):
        _, ch_i = sorted_num[i]
        if not front[ch_i]:
            del sorted_num[i]
            break

answer = 0
m = 9
for n, _ in reversed(sorted_num):
    answer += n * m
    m -= 1
print(answer)