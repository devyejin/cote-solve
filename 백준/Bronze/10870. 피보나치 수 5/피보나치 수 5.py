def fibo(n):

    memo = [-1] * (n+1) #메모이제이션 초기화

    if n <= 1:
        return n

    memo[0] = 0
    memo[1] = 1

    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

print(fibo(int(input())))