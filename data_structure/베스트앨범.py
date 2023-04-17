# https://school.programmers.co.kr/learn/courses/30/lessons/42579#

def solution(genres, plays):
    info = dict()
    for i, g in enumerate(genres):
        if g not in info:
            info[g] = [0, []] # [sum of play nums, list of (play num, index)]
        info[g][0] += plays[i]
        info[g][1].append((plays[i], i)) 
        
    for g in info:
        info[g][1].sort(key=lambda x:(-x[0], x[1])) # add '-' for sorting descending order
        
    gOrder = sorted(info.values(), key=lambda x:x[0], reverse=True)
    # print(gOrder)
    
    answer = []
    for _ , sortedSongs in gOrder:
        for i in range(min(2, len(sortedSongs))):
            answer.append(sortedSongs[i][1])
        
    return answer