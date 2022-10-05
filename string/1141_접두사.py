# https://www.acmicpc.net/problem/1141
import sys
N = int(sys.stdin.readline())
words = sorted([sys.stdin.readline().rstrip() for _ in range(N)])
cnt = 1 # 마지막 단어는 무조건 포함됨
for w in range(len(words)-1):
    # 하나 이상의 다른 단어의 접두사가 된다면 최대 접두사X 부분 집합에 포함하지 않음.
    if not words[w+1].startswith(words[w]):
        cnt += 1
print(cnt)
