# https://www.acmicpc.net/problem/1148
import sys

N = ord('Z') - ord('A') + 1

def count_alpha(word):
    cnt = [0] * N
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
    
    word_cnt = [0] * N # word_cnt[i]: i번 째 알파벳을 포함하고 있는 단어의 개수
    
    for w_cnt in words:
        include = True
        for p, w in zip(p_cnt, w_cnt): # 퍼즐의 알파벳으로 만들 수 있는 단어인지 확인
            if p < w:
                include = False
                break
        if include: # 만들 수 있는 단어일 경우 word_cnt 업데이트
            for i in range(len(word_cnt)):
                if w_cnt[i] > 0:
                    word_cnt[i] += 1
    
    exist_alpha = [False] * N
    for ch in puzzle:
        exist_alpha[ord(ch)-ord('A')] = True
    
    cnt_for_puzzle = [word_cnt[i] for i in range(N) if exist_alpha[i]]
    m = min(cnt_for_puzzle)
    M = max(cnt_for_puzzle)
    min_alpha = [chr(i + ord('A')) for i in range(N) if exist_alpha[i] and word_cnt[i] == m]
    max_alpha = [chr(i + ord('A')) for i in range(N) if exist_alpha[i] and word_cnt[i] == M]
    print("".join(min_alpha), m, "".join(max_alpha), M)