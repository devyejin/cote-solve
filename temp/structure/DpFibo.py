#Top down 방식 + memoization 활용

memo = {}

def fibo(n):
    if n == 1 or n == 2: #base condition
        return 1
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(5))


memo = {}
memo[1] = 1
memo[2] = 1

def fibo(n):
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
        return memo[n]