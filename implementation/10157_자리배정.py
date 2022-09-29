# https://www.acmicpc.net/problem/10157
R, C = map(int, input().split())
k = int(input())
max_k = R * C

if k > max_k:
    print(0)
else:
    m = min(R, C)
    start = 1
    for d in range((m // 2) + (m % 2)):
        d2 = d + d
        r = R - d2
        c = C - d2
        end = start + (r + c) * 2 - 4
        # print(start, end)
        if k < end:
            bound = start + c - 1
            diff = k - start
            if k < bound:
                print(d + 1, d + 1 + diff)
                break
            bound += r - 1
            diff -= c - 1
            if k < bound:
                print(d + 1 + diff, C - d)
                break
            bound += c - 1
            diff -= r - 1
            if k < bound:
                print(R - d, C - d - diff)
                break
            bound += r - 1
            diff -= c - 1
            if k < bound:
                print(R - d - diff, d + 1)
                break
        start = end
