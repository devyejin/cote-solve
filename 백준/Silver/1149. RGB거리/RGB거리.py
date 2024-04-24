n = int(input())
d = [0] * n

for i in range(n):
    #한 줄씩 읽어서 a에 넣기
    d[i] = list(map(int, input().split())) # split() 쓰면 str되서 map이용

for k in range(1,n):
    d[k][0] = min(d[k-1][1], d[k-1][2]) + d[k][0]
    d[k][1] = min(d[k-1][0], d[k-1][2]) + d[k][1]
    d[k][2] = min(d[k-1][0], d[k-1][1]) + d[k][2]

print(min(d[n-1][0], d[n-1][1], d[n-1][2] ))