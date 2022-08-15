# https://www.acmicpc.net/problem/9996
import sys
N = int(sys.stdin.readline())
front, back = sys.stdin.readline().strip().split("*")
for _ in range(N):
    name = sys.stdin.readline().strip()
    if len(name) >= len(front) + len(back) and front == name[:len(front)] and back == name[-len(back):]:
        print("DA")
    else:
        print("NE")
    