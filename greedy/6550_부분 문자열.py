# https://www.acmicpc.net/problem/6550
import sys

lines = sys.stdin.readlines()
for line in lines:
    s, t = line.split()
    idx = -1
    for ch in s:
        idx = t.find(ch, idx+1)
        if idx == -1:
            print("No")
            break
    if idx != -1:
        print("Yes")