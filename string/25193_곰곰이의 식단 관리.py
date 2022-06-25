# https://www.acmicpc.net/problem/25193
import math
N = int(input())
s = input()
cnt_c = s.count("C")
cnt_else = len(s) - cnt_c
print(math.ceil(cnt_c / (cnt_else + 1)))