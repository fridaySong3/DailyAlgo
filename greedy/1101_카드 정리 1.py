# https://www.acmicpc.net/problem/1101
import sys
N, M = map(int, sys.stdin.readline().split())

oneColor = [0] * M # oneColor[m]: m번째 색만 담고있는 박스의 존재 여부
cntOneColor = 0 # oneColor의 1의 개수
cntEmpty = 0 # 빈 박스 개수

for _ in range(N):
    box = list(map(int, sys.stdin.readline().split()))
    cnt0 = box.count(0)
    if cnt0 == M:
        cntEmpty += 1
    elif cnt0 == M - 1:
        for m in range(M):
            if box[m] != 0:
                if oneColor[m] == 0:
                    oneColor[m] = 1
                    cntOneColor += 1
                break
                
# 최소 이동 횟수 = 전체 박스 개수 - 움직이지 않아도 되는 박스 개수 (빈 박스, oneColor 박스, 조커 박스)
answer = N - cntEmpty - cntOneColor - 1
# 모든 박스가 빈 박스 또는 oneColor 박스일 경우, 조커 박스까지 빼주면 음수가 되므로 0 출력
print(0 if answer < 0 else answer)