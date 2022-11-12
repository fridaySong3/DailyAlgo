# https://www.acmicpc.net/problem/20436
keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
end_l = [5, 5, 4]
key = dict()
for r in range(len(keyboard)):
    for c in range(len(keyboard[r])):
        key[keyboard[r][c]] = (r, c)

sl, sr = input().split()
string = input().rstrip()
sl = key[sl]
sr = key[sr]

time = 0
for ch in string:
    r, c = key[ch]
    if c < end_l[r]:
        time += abs(sl[0] - r) + abs(sl[1] - c)
        sl = (r, c)
    else:
        time += abs(sr[0] - r) + abs(sr[1] - c)
        sr = (r, c)
print(time + len(string))