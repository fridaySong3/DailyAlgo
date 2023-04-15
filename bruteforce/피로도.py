# https://school.programmers.co.kr/learn/courses/30/lessons/87946

answer = 0

def dfs(k, cnt, dungeons, visit):
    global answer
    answer = max(answer, cnt)
    for i in range(len(visit)):
        if not visit[i] and k >= dungeons[i][0]:
                visit[i] = True
                dfs(k-dungeons[i][1], cnt+1, dungeons, visit)
                visit[i] = False
        
def solution(k, dungeons):
    global answer
    visit = [False] * len(dungeons)
    dfs(k, 0, dungeons, visit)
    return answer