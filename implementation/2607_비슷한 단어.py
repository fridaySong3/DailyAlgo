# https://www.acmicpc.net/problem/2607
import sys

alph_num = ord('Z') - ord('A') + 1

def count(word):
    cnt = [0 for _ in range(alph_num)]
    for ch in word:
        cnt[ord(ch) - ord('A')] += 1
    return cnt

def is_similar(diff):
    return (diff.count(0) == alph_num) or \
        (diff.count(0) == (alph_num - 1)) and (diff.count(1) == 1 or diff.count(-1) == 1) or \
        (diff.count(0) == (alph_num - 2)) and (diff.count(1) == 1 and diff.count(-1) == 1)

N = int(sys.stdin.readline())
base = sys.stdin.readline().rstrip()
b_cnt = count(base)
answer = 0
for _ in range(N-1):
    word = sys.stdin.readline().rstrip()
    w_cnt = count(word)
    diff = [b - w for b, w in zip(b_cnt, w_cnt)]
    if is_similar(diff):
        answer += 1
print(answer)
