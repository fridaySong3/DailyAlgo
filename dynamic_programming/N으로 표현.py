# https://school.programmers.co.kr/learn/courses/30/lessons/42895#

def op(setA, setB):
    result = set()
    for a in setA:
        for b in setB:
            result.add(a+b)
            result.add(a-b)
            result.add(b-a)
            result.add(a*b)
            if b != 0:
                result.add(a//b)
            if a != 0:
                result.add(b//a)
    return result

def solution(N, number):
    answer = -1
    END = 9
    usedNum = [None] # usedNum[i] = N을 i개 사용해서 만들 수 있는 수의 집합

    for i in range(1, END):
        # N만으로 만들 수 있는 수 넣기
        result = set([ int(str(N)*i) ])
        
        # 사칙연산으로 만들 수 있는 수 넣기
        for j1 in range(1, i//2+1):
            j2 = i - j1
            result.update( op(usedNum[j1], usedNum[j2]) )
        
        # number가 있는지 확인
        if number in result:
            answer = i
            break
        
        # 더 적은 횟수 사용해서 만들 수 있는 숫자 제거
        for h in range(1, i):
            result -= usedNum[h]
        
        # print(i, result)
        usedNum.append(result)
        
    return answer