n, k = map(int, input().split())
result = 0 

while True:
    target = (n // k) * k #n이 k로 나눠떨어지지 않을 때, n이 k로 나눠 떨어지는 가장 가까운 수
    result += (n - target) #k의 배수가 되도록 -1을 빼는 연산 횟수를 더해주고
    n = target #그만큼 뺐으니, n은 target(k의 배수) 가 됨
    
    if n < k: #n이 k보다 작다면
        break
    #n이 k보다 크다면 k로 나누기
    n //= k
    result += 1

#마지막으로 남은 수에 대해서 1빼기 연산 (만약 n=3, k=4라면, n이 1이 되기까지 2번빼야하니까 n-1)
result += (n-1)
print(result)