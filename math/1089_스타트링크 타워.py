# https://www.acmicpc.net/problem/1089
import sys

# strNum에서 숫자 하나씩, 빛이 나는 곳만 1로 만들어 binary로 표현하여 binNum에 담아 반환
def toBinary(strNum, binNum):
    nums = (len(strNum[0]) + 1) // 4
    for i in range(nums):
        startC = 4 * i
        for r in range(R):
            for c in range(C):
                if strNum[r][startC + c] == "#":
                    binNum[i] |= (1 << (r * C + c))
                
R, C = 5, 3
ALL = '''\
###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###\
'''
ALL = ALL.split()
binAll = [0] * 10
toBinary(ALL, binAll)

N = int(sys.stdin.readline())
inp = [sys.stdin.readline().rstrip() for _ in range(R)]
binInp = [0] * N
toBinary(inp, binInp)

candidate = [[] for _ in range(N)]
for i in range(N):
    for j in range(10):
        # 0이어야 할 곳이 1인 경우가 없다면, j가 될 가능성이 있는 입력
        if (binInp[i] | binAll[j]) == binAll[j]:
            candidate[i].append(j)
    # i번 째 입력이 될 수 있는 숫자가 없다면 -1 출력
    if len(candidate[i]) == 0:
        print(-1)
        exit()

# 모든 수의 평균 = 각 자릿수의 평균의 합
answer = sum([sum(c) * (10**(N-i-1)) / len(c) for i, c in enumerate(candidate)])
print(answer)
