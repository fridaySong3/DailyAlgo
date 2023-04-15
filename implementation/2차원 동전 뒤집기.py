# https://school.programmers.co.kr/learn/courses/30/lessons/131703

def find_true(arr):
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == True:
                return r, c
    return -1, -1

def make_all_false(diff):
    ans = 0
    flipped_r = [False for _ in range(len(diff))]
    flipped_c = [False for _ in range(len(diff[0]))]
    while True:
        r, c = find_true(diff)
        if r == -1:
            break
        if not flipped_r[r]:
            flipped_r[r] = True
            for cc in range(len(diff[r])):
                diff[r][cc] = not diff[r][cc]
        elif not flipped_c[c]:
            flipped_c[c] = True
            for rr in range(len(diff)):
                diff[rr][c] = not diff[rr][c]
        else:
            ans = -1
            break
        ans += 1
    return ans

def solution(beginning, target):
    R, C = len(target), len(target[0])
    answer = 0
    diff = [[False if beginning[r][c] == target[r][c] else True for c in range(C)] for r in range(R)]
    # print(diff)
    
    answer = make_all_false(diff)
    answer = min(answer, R + C - answer)
    return answer