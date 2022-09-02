N, K = map(int, input().split())
kit = list(map(int, input().split()))
cnt = 0

def dfs(visit, weight):
    global cnt
    if all(visit):
        cnt += 1
        return
    for i in range(N):
        if not visit[i]:
            tmp_w = weight + kit[i] - K
            if tmp_w < 0:
                continue
            visit[i] = True
            dfs(visit, tmp_w)
            visit[i] = False

visit = [False for _ in range(N)]
weight = 0
dfs(visit, weight)

print(cnt)