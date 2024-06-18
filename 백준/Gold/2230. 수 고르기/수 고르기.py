N, M = map(int, input().split())

nums = []
result = float('inf')
for _ in range(N):
    nums.append(int(input()))

nums.sort() #O(nlogn)

s, e = 0, 0

while e < N and s <= e: #idx이전까지
    if nums[e] - nums[s] >= M:
        result = min(result, nums[e] - nums[s])
        s += 1 
    else:
        e += 1

print(result)
    
    