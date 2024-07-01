N, S = map(int, input().split())
nums = list(map(int, input().split()))

print(nums)

count = 0
e = 0
interval_sum = 0

for s in range(N):
    while interval_sum < S and e < N:
        interval_sum += nums[e]
        e += 1
    if interval_sum == S:
        count += 1
    # interval_sum > S이거나 == S일 때 e>=N이라  s+= 1 이동
    interval_sum -= nums[s]

print(count)