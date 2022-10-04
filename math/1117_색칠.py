# https://www.acmicpc.net/problem/1117
W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
bound = min(f, W - f)
left = max(0, min(x2, bound) - x1) # bound 기준, 왼쪽 가로 길이
right = max(0, x2 - max(x1, bound)) # bound 기준, 오른쪽 가로 길이
print(W * H - (c + 1) * (y2 - y1) * ((2 * left) + right))