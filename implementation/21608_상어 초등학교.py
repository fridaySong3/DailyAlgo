# acmicpc.net/problem/21608
import sys
from collections import Counter

N = int(sys.stdin.readline())
ST_NUM = N*N
arr = [[0 for _ in range(N)] for _ in range(N)]

DR = [0, 1, 0, -1]
DC = [1, 0, -1, 0]

seat = [None for _ in range(ST_NUM + 1)]
st_info = [None for _ in range(ST_NUM + 1)]

for st in range(ST_NUM):
     st_num, *favorite = list(map(int, sys.stdin.readline().split()))
     st_info[st_num] = favorite
     
     f_adj = []
     for i in range(len(favorite)):
          if seat[favorite[i]] == None:
               continue
          r, c = seat[favorite[i]]
          for dr, dc in zip(DR, DC):
               nr, nc = r + dr, c + dc
               if 0 <= nr < len(arr) and 0 <= nc < len(arr) and arr[nr][nc] == 0:
                    f_adj.append((nr, nc))
     
     if len(f_adj) > 0:
          cnt = Counter(f_adj).most_common()
          candidate = [loc for loc, c in cnt if c == cnt[0][1]]
          if len(candidate) == 1:
               r, c = candidate[0]
               arr[r][c] = st_num
               seat[st_num] = (r, c)
               continue
     else:
          candidate = [(r, c) for r in range(N) for c in range(N) if arr[r][c] == 0]
     
     adj_empty_num = [0 for _ in range(len(candidate))]
     for i in range(len(candidate)):
          r, c = candidate[i]
          for dr, dc in zip(DR, DC):
               nr, nc = r + dr, c + dc
               if 0 <= nr < len(arr) and 0 <= nc < len(arr) and arr[nr][nc] == 0:
                    adj_empty_num[i] += 1
     
     M = max(adj_empty_num)
     candidate = [candidate[i] for i, n in enumerate(adj_empty_num) if n == M]
     if len(candidate) == 1:
          r, c = candidate[0]
          arr[r][c] = st_num
          seat[st_num] = (r, c)
          continue
     
     r, c = min(candidate)
     arr[r][c] = st_num
     seat[st_num] = (r, c)

score = [0, 1, 10, 100, 1000]
ans = 0
for st in range(1, ST_NUM+1):
     f_adj_num = 0
     r, c = seat[st]
     for dr, dc in zip(DR, DC):
          nr, nc = r + dr, c + dc
          if 0 <= nr < len(arr) and 0 <= nc < len(arr) and arr[nr][nc] in st_info[st]:
               f_adj_num += 1
     ans += score[f_adj_num]
print(ans)