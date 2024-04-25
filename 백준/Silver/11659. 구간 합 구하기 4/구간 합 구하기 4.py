import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]

sum = 0

for i in arr:
    sum += i
    prefix_sum.append(sum) #누적 합

for K in range(n):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
