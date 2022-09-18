# https://www.acmicpc.net/problem/16953
A, B = map(int, input().split())
op_num = 0
while True:
    if A == B:
        print(op_num + 1)
        break
    if A > B:
        print(-1)
        break
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        print(-1)
        break
    op_num += 1