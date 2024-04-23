# n은 11보다 작음

d = [0] * 11 # dp테이블
d[1], d[2], d[3] = 1,2,4 #초기값

for i in range(4,11):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for i in range(0, int(input())):
    print(d[int(input())])


