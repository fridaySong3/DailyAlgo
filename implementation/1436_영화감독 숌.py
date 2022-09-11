# https://www.acmicpc.net/problem/1436
N = int(input())
base = "666"
prefix = 0
i = 1
while True:
    num = str(prefix) + base
    base_loc = num.find(base)
    if base_loc != len(num) - len(base):
        zero_num = len(num) - base_loc - len(base)
        n = int(num[:base_loc] + base + "0" * zero_num)
        for _ in range(10**zero_num):
            if i == N:
                print(n)
                exit()
            n += 1
            i += 1
        prefix += 1
        num = str(prefix) + base
        
    if i == N:
        print(int(num))
        exit()
    prefix += 1
    i += 1