# https://www.acmicpc.net/problem/1148
import sys

def count_alpha(word):
    cnt = [0] * (ord('Z') - ord('A') + 1)
    for ch in word:
        cnt[ord(ch)-ord('A')] += 1
    return cnt

words = []
while True:
    word = sys.stdin.readline().rstrip()
    if word == "-":
        break
    words.append(count_alpha(word))
    
while True:
    puzzle = sys.stdin.readline().rstrip()
    if puzzle == "#":
        break
    p_cnt = count_alpha(puzzle)
    
    alpha_cnt = [0] * (ord('Z') - ord('A') + 1)
    for w_cnt in words:
        include = True
        for p, w in zip(p_cnt, w_cnt):
            if p < w:
                include = False
                break
        if include:
            for i in range(len(alpha_cnt)):
                if w_cnt[i] > 0:
                    alpha_cnt[i] += 1
    
    not_exist = [ch for ch in puzzle if alpha_cnt[ord(ch)-ord('A')] == 0]
    
    if len(not_exist) == 9:
        not_exist = sorted(list(set(not_exist)))
        print("".join(not_exist), 0, "".join(not_exist), 0)
    else:
        if len(not_exist) > 0:
            not_exist = sorted(list(set(not_exist)))
            print("".join(not_exist), 0, end=" ")
            ma = max(alpha_cnt)
        else:
            sort = sorted(set(alpha_cnt))
            mi, ma = sort[1], sort[-1]
            mi_list = [i for i in range(len(alpha_cnt)) if mi == alpha_cnt[i]]
            print("".join(map(lambda x: chr(ord('A')+x), mi_list)), mi, end=" ")
        
        ma_list = [i for i in range(len(alpha_cnt)) if ma == alpha_cnt[i]]
        print("".join(map(lambda x: chr(ord('A')+x), ma_list)), ma)
