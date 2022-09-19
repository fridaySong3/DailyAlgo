# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW9j74FacD0DFAUY&
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    R = [int(input()) for _ in range(N)]
    W = [0]
    W.extend([int(input()) for _ in range(M)])
    in_out = [int(input()) for _ in range(2 * M)]
    parking = [False] * N
    where = [-1] * (M+1)
    ans = 0
    for i in range(len(in_out)):
        if in_out[i] < 0:    # out
            car = -in_out[i]
            if where[car] == -1:
                continue
            parking[where[car]] = False
            where[car] = -1
        else:    # in
            car = in_out[i]
            try:
                loc = parking.index(False)
            except ValueError: # 주차장에 빈 자리가 없을 경우
                # 빈 자리 만들어서 loc에 대입
                for j in range(i+1, len(in_out)):
                    if in_out[j] < 0:    # out
                        out_car = -in_out[j]
                        if where[out_car] == -1:
                            continue
                        loc = where[out_car]
                        parking[where[out_car]] = False
                        where[out_car] = -1
                        break
            parking[loc] = True
            where[car] = loc
            ans += R[loc] * W[car]
    print("#", test_case, " ", ans, sep="")