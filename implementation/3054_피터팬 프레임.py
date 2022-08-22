# https://www.acmicpc.net/problem/3054
import sys

def decorate(arr, deco, start, ch):
    arr[2][start] = ch
    d = [0, 1, 2, 1, 0]
    for i in range(len(d)):
        arr[i][start-d[i]] = deco
        arr[i][start+d[i]] = deco

string = sys.stdin.readline().rstrip()
col = len(string) * 4 + 1
result = [['.' for _ in range(col)] for _ in range(5)]
for i in range(len(string)):
    if i % 3 == 2:
        continue
    decorate(result, '#', i*4+2, string[i])
for i in range(2, len(string), 3):
    decorate(result, '*', i*4+2, string[i])

for row in result:
    print(''.join(row))