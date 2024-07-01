N = 5
M = 5
nums = [1,2,3,2,5]
# 부분 수열의 합이 M 인 부분 연속 수열의 개수는?
count = 0
interval_sum = 0
e = 0

#start를 차례로 증가시키며 반복 
for s in range(N): 
    # end를 가능한 만큼 이동시키기 (case1)
    while interval_sum < M and e < N:
        interval_sum += nums[e]
        e += 1
    #조건 불충족시 e값을 증가시키다가, 조건(=M) 충족시 s값을 증가 (case2)
    if interval_sum == M:
        count += 1
    interval_sum -= nums[s] #for문 내에 있으니, s값 이동시키기 전에 합에서 기존 s값 뺌

print(count)