# https://www.acmicpc.net/problem/4889
n = 1
while True:
    line = list(input().rstrip())
    if line[0] == '-':
        break
    i = 1
    ans = 0
    while i < len(line):
        if i > 0 and line[i-1] == '{' and line[i] == '}':
            del line[i-1: i+1]
            i -= 1
        else:
            i += 1
            
    for i in range(0, len(line), 2):
        if line[i] == "}" and line[i+1] == "{":
            ans += 2
        else:
            ans += 1
    print(n, end=". ")
    print(ans)
    n += 1
