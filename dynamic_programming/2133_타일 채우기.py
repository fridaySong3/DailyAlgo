# https://www.acmicpc.net/problem/2133
N = int(input())
if N % 2 == 1:
    print(0)
else:
    DP = [0 for i in range(N+1)]
    DP[0] = 1
    DP[2] = 3
    for i in range(4, N+1, 2):
        DP[i] = DP[i-2] * DP[2] + (DP[i-2] - DP[i-4])
        # DP[i-4] => N이 i-2일 때 마지막 2열이 '1x2 타일로 이루어진 3x2 타일'로 이루어진 경우의 수
        # 위의 경우를 제외한 D[i-2]의 타일들은 뒤에 2열을 추가했을 때(즉 N=i일 때) 마지막 3열이 =|의 형태로 끝날 수 있음.
        
    print(DP[N])