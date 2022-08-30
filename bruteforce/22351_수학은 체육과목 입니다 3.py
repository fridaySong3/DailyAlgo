# https://www.acmicpc.net/problem/22351
import sys
S = sys.stdin.readline()[:-1]

for first_len in range(1, 3):
    first = int(S[:first_len])
    inc = 1
    num = str(first + inc)
    beg = first_len
    end = beg + len(num)
    while end <= len(S):
        if num != S[beg:end]:
            break
        inc += 1
        num = str(first + inc)
        beg = end
        end = beg + len(num)
    if beg == len(S):
        print(first, int(num)-1)
        exit()

print(S[:3], S[-3:])
