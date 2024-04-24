
n = int(input()) # 계단의 수
stairs = [0] * 301 # 계단이 300까지 가능하다 했으니까
for i in range(1, n+1):
    stairs[i] = int(input()) # 계단 점수

if n == 1:
    print(stairs[1])
    exit() #프로그램 종료

if n == 2:
    print(stairs[1] + stairs[2])
    exit()
    
d = [[0] * 3 for _ in range(n+1)]

d[1][1] = stairs[1]
d[1][2] = 0
d[2][1] = stairs[2]
d[2][2] = stairs[1] + stairs[2]

for i in range(3, n+1):
    d[i][1] = max(d[i-2][1], d[i-2][2]) + stairs[i]
    d[i][2] = d[i-1][1] + stairs[i]

# n번쨰 올랐을 떄 최댓값
print(max(d[n][1], d[n][2]))