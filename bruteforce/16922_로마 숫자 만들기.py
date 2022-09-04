N = int(input())
kind = [1, 5, 10, 50]
nums = set()

def bruteforce(idx, n, num):
    if n == 0:
        nums.add(num)
        return
    if idx == len(kind) - 1:
        bruteforce(idx + 1, 0, num + kind[idx] * n)
    else:
        for i in range(n+1):
            bruteforce(idx + 1, n - i, num + kind[idx] * i)

bruteforce(0, N, 0)
print(len(nums))