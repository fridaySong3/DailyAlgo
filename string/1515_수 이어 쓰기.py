# https://www.acmicpc.net/problem/1515
strNum = input().rstrip()

i = 0
n = 1
ni_limit = -1
while i < len(strNum):
    ni = str(n).find(strNum[i], ni_limit+1)
    if ni > ni_limit: # found
        i += 1 # next strNum
        ni_limit = ni
    else: # not found
        n += 1 # next n
        ni_limit = -1
print(n)