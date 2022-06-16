# https://www.acmicpc.net/problem/1013
import sys

def pattern1(signal, i):
    p = "100+1+"
    for j in range(len(p)):
        if p[j] == "+":
            if j == len(p)-1:
                while signal[i] == p[j-1]:
                    matched, end = pattern1(signal, i)
                    if matched:
                        i = end
                        return True, i
                    i += 1
                    if i == len(signal):
                        return True, i
            else:
                while signal[i] == p[j-1]:
                    i += 1
                    if i == len(signal):
                        return False, i
        elif p[j] == signal[i]:
            i += 1
            if i == len(signal):
                if (j == len(p) - 1) or (j == len(p) - 2 and p[-1] == "+"):
                    return True, i
                else:
                    return  False, i
        else:
            return False, i
    return True, i

def pattern2(signal, i):
    p = "01"
    if signal[i:i+len(p)] == p:
        return True, i+len(p)
    else:
        return False, -1

patterns = [pattern1, pattern2]

T = int(sys.stdin.readline())
for _ in range(T):
    signal = sys.stdin.readline().strip()        
    i = 0
    while i < len(signal):
        prev_i = i
        for pattern in patterns:
            matched, end = pattern(signal, i)
            if matched:
                i = end
                break
        if prev_i == i:
            break
            
    if i < len(signal):
        print("NO")
    else:
        print("YES")
            