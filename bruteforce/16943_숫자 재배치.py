# https://www.acmicpc.net/problem/16943
A, B = input().split()
if len(A) > len(B):
    print(-1)
elif len(A) < len(B):
    print(''.join(sorted(A, reverse=True)))
else:
    num_b = int(B)
    A = list(A)
    smallest = sorted(A)
    for i in range(len(smallest)):
        if smallest[i] != '0':
            if i != 0:
                smallest[0], smallest[i] = smallest[i], smallest[0]
            break
    A.sort(reverse=True)
    while True:
        num_a = int(''.join(A))
        if num_a < num_b:
            print(num_a)
            break
        if A == smallest:
            print(-1)
            break
        for i in range(len(A)-1, 0, -1):
            if A[i-1] > A[i]:
                for j in range(len(A)-1, i-1, -1):
                    if A[i-1] > A[j]:
                        A[i-1], A[j] = A[j], A[i-1]
                        A = A[:i] + list(reversed(A[i:]))
                        break
                break
        