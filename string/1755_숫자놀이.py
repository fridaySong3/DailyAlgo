# https://www.acmicpc.net/problem/1755
alph = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
M, N = map(int, input().split())
num = [str(i) for i in range(M, N+1)]
num.sort(key=lambda x: [alph[int(i)] for i in x])
for i, n in enumerate(num):
    print(n, end=' ')
    if i % 10 == 9:
        print()