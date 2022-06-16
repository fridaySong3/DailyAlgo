import sys

N = 5000
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
base = [0 for _ in range(N*2+1)]
arr = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

def arr_to_str():
    max_len = len(str(max(map(max, arr))))
    arr_str = []
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            num = str(arr[r][c])
            arr_str.append(' ' * (max_len - len(num)))
            arr_str.append(num)
            arr_str.append(' ')
        arr_str.append('\n')
    return ''.join(arr_str)

def l_p(logical):
    return logical + N
 
base[l_p(0)] = 1
prev_increment = 0
for i in range(1, N+1):
    base[l_p(-i)] = base[l_p(i-1)] + prev_increment + 2
    prev_increment += 2
    base[l_p(i)] = base[l_p(-i)] + prev_increment + 2
    prev_increment += 2

for r in range(r1, r2+1):
    for c in range(c1, c2+1):
        pr, pc = r - r1, c - c1
        if (r < 0 and r <= c <= -r) or (r >= 0 and -r <= c <= r+1):
            br, bc = r, -r
            arr[pr][pc] = base[l_p(br)] + abs(bc - c)
        else:
            br, _ = -c, c
            arr[pr][pc] = base[l_p(br)] - abs(br - r)

print(arr_to_str(), end='')