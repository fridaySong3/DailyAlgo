# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        idx = 0
        possible = True
        for c in st:
            loc = skill.find(c)
            if loc != -1:
                if loc != idx:
                    possible = False
                    break
                else:
                    idx += 1
        if possible:
            answer += 1
    return answer