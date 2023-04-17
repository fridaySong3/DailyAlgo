# https://school.programmers.co.kr/learn/courses/30/lessons/42579#

def solution(genres, plays):
    info = dict()
    for i, g in enumerate(genres):
        if g not in info:
            info[g] = [0, []] # [sum of play nums, list of (play num, index)]
        info[g][0] += plays[i]
        info[g][1].append((plays[i], i)) 
        
    gOrder = sorted(info.keys(), key=lambda g:info[g][0], reverse=True)
    # print(gOrder)
    
    answer = []
    for g in gOrder:
        sortedSongsIdx = [song[1] for song in sorted(info[g][1], key=lambda x:(-x[0], x[1]))] # add '-' for sorting descending order
        answer += sortedSongsIdx[:min(2, len(sortedSongsIdx))]
        
    return answer