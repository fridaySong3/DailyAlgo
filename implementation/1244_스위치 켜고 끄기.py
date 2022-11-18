# https://www.acmicpc.net/problem/1244
import sys

def male_do(n):
    global switches
    for i in range(n, len(switches), n):
        switches[i] = (1 if switches[i] == 0 else 0)
    
def female_do(n):
    global switches
    switches[n] = (1 if switches[n] == 0 else 0)
    for i in range(1, min(n, len(switches)-n)):
        if switches[n-i] == switches[n+i]:
            switches[n-i] = (1 if switches[n-i] == 0 else 0)
            switches[n+i] = switches[n-i]
        else:
            break
            
manipulate = (male_do, female_do)

SW_N = int(sys.stdin.readline())
switches = [0]
switches.extend(map(int, sys.stdin.readline().split()))
ST_N = int(sys.stdin.readline())
students = [tuple(map(int, sys.stdin.readline().split()))
            for _ in range(ST_N)]

for gender, num in students:
    manipulate[gender-1](num)
    
for i in range(1, len(switches), 20):
    if (i + 20) > len(switches):
        print(" ".join(map(str, switches[i:])))
    else:
        print(" ".join(map(str, switches[i:i+20])))