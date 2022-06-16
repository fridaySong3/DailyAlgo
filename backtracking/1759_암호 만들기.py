import sys

L, C = map(int, sys.stdin.readline().split())
alpha = sys.stdin.readline().split()
alpha.sort()
m_list = ['a', 'e', 'i', 'o', 'u']

j_m_num = [[0, 0] for _ in range(len(alpha))]
for i in reversed(range(len(alpha))):
    if i != len(alpha)-1:
        j_m_num[i][0] = j_m_num[i+1][0]
        j_m_num[i][1] = j_m_num[i+1][1]
    if alpha[i] in m_list:
        j_m_num[i][1] += 1
    else:
        j_m_num[i][0] += 1
# print(j_m_num)

least_j = 2
least_m = 1

result = []


def is_promising(cur_i, pswd, j_num, m_num):
    return (L-len(pswd) <= C-cur_i) and (least_j - j_num <= j_m_num[cur_i][0]) and (least_m - m_num <= j_m_num[cur_i][1])


def backtracking(cur_i, pswd, j_num, m_num):
    if len(pswd) == L and j_num >= least_j and m_num >= least_m:
        result.append("".join(pswd))
        return
    if cur_i >= len(alpha):
        return
    if not is_promising(cur_i, pswd, j_num, m_num):
        return

    # alpha[cur_i]를 넣는 경우
    pswd.append(alpha[cur_i])
    if alpha[cur_i] in m_list:
        backtracking(cur_i+1, pswd, j_num, m_num+1)
    else:
        backtracking(cur_i+1, pswd, j_num+1, m_num)
    del pswd[-1]
    
    # alpha[cur_i]를 안 넣는 경우
    backtracking(cur_i+1, pswd, j_num, m_num)


backtracking(0, [], 0, 0)
result.sort()
for i in result:
    print(i)
