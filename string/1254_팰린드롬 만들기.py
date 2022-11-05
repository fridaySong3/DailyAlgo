# https://www.acmicpc.net/problem/1254
S = input().rstrip()

def is_palin(i, j):
    global S
    palin = True
    while i < j:
        if S[i] == S[j]:
            i += 1
            j -= 1
        else:
            palin = False
            break
    return palin

for s in range(len(S)):
    if is_palin(s, len(S)-1):
        break
print(len(S) + s)