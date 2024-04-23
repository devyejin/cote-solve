# n은 11보다 작음

d = [0] * 11 # dp테이블
d[1], d[2], d[3] = 1,2,4 #초기값

for i in range(4,11):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for i in range(0, int(input())):
    print(d[int(input())])




# 가독성 개선 -- 내부에서는 계속 입력을 반복해서 받아야하니까(반복->함수)

def get_input():
    return int(input())

d = [0] * 11 #dp 테이블
d[1], d[2], d[3] = 1,2,4 #초기값

for i in range(4, 11):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

num_cases = get_input()
for _ in range(num_cases):
    x = get_input()
    print(d[x])
