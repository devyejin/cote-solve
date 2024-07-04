# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split())) #각 줄에서 최솟값 뽑기
    min_value = min(data)
    result = max(min_value, result) # 최솟값들 중 max로 result 갱신

print(result)