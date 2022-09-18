# https://www.acmicpc.net/problem/15904
import sys
result = "UCPC"
string = sys.stdin.readline()
i = 0
for ch in string:
    if ch == result[i]:
        i += 1
        if i == len(result):
            print("I love UCPC")
            break
if i != len(result):
    print("I hate UCPC")