n = int(input()) # 삼각형 크기
d=[] #dp테이블

for i in range(n):
    d.append(list(map(int,input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            d[i][j] += d[i-1][j]
        elif j == i:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] =  max(d[i-1][j-1] + d[i][j], d[i-1][j]+d[i][j])

#리스트 값들 중 max값
print(max(d[n-1]))