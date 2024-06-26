N = int(input())
A = list(map(int, input().split()))

d = [1] * N #d[i] : A[i]를 마지막 원소로 하는 가장 긴 감소하는 수율

for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))