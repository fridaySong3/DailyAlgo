# https://www.acmicpc.net/problem/1269
import sys
sys.stdin.readline()
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))
print(len(A ^ B))