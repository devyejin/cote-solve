n, m = map(int, input().split())
result = 0


for i in range(n):
    data = list(map (int, input().split()))
        #현재 행에거 가장 작은 수 찾기
        # for d in range(m): 인덱스로 돌 필요 없음!
    min_value = 1001 # <--- 각 행에서 최솟값 찾기 전 갱신
    for d in data:
            min_value = min(d, min_value) #작은 값으로 갱신
    #각 행에서 가장 작은 값들 중 큰 수 갱신
    result = max(result, min_value)

print(result)
            