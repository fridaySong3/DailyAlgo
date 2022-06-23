import sys

def to_bit(word):
    bit = 0
    for x in map(lambda ch: 1<<(ord(ch)-ord('a')), word):
        bit |= x
    return bit

def count_read(teach):
    cnt = 0
    for word in words:
        if word & teach == word:
            cnt += 1
    return cnt
    
def backtracking(left, start, teach):
    if left == 0:
        return count_read(teach)
    cnt_read = 0
    for i in range(start, 26):
        new_alpha = 1 << i
        if teach & new_alpha == 0:
            cnt_read = max(cnt_read, backtracking(left-1, i+1, teach | new_alpha))
    return cnt_read
    
N, K = map(int, sys.stdin.readline().split())

words = []
for i in range(N):
    words.append(to_bit(sys.stdin.readline()[4:-5]))

if K < 5:
    print(0)
    exit()

teach = to_bit("antic")
answer = backtracking(K-5, 0, teach)    
print(answer)