data = list(map(int, input()))
result = 0 # 0일 때 정답인건데, 만약 데이터가 잘못들어오는경우 예외처리가 안될텐데

for i in range(len(data)//2):
    result += (data[i] - data[len(data)-1-i])

if result == 0:
    print('LUCKY')
else:
    print('READY')