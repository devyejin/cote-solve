N, M = map(int, input().split())
nums = list(map(int, input().split()))

i, j = 0, 0
current_sum = 0
answer = 0

while j < N:
    if  current_sum < M:
        current_sum += nums[j] 
        j += 1
    while current_sum >= M:
        if current_sum == M:
            answer += 1
        current_sum -= nums[i] # 기존 합 중 i값 빼기
        i += 1
        
print(answer)