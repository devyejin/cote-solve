import sys
input = sys.stdin.readline

N = int(input()) # 수열 A의 크기
A = list(map(int, input().split()))

dp = [1] * N

#보텀업 방식
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
