n, k = map(int, input().split())
result = 0 #연산 횟수

while n > 1:
    if n % k == 0: #나누어 떨어진다면
        n = n // k
        result += 1
    else:
        n -= 1
        result += 1

print(result)
        