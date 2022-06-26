# https://www.acmicpc.net/problem/2941
word = input()

i = 0
cnt = 0
while i < len(word):
    if word[i] == "=":
        if i-2 >= 0 and word[i-2:i] == "dz":
            cnt -= 1
    elif not(word[i] == "-" or (word[i] == "j" and i-1 >= 0 and (word[i-1] == "l" or word[i-1] == "n"))):
        cnt += 1
    i += 1
print(cnt)