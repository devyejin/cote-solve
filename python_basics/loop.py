#반복문 for, while -> for문을 더 많이 사용

#1~9까지의 합
i = 1
result = 0

while i <= 9:
    result += i
    i += 1
    
print(result) #45

#1~9까지 중 홀수의 합
i = 1
result = 0

while i<= 9:
    if i % 2 == 1:
        result += i
    i += 1
    
print(result) #25

#for문
i = 1
result = 0

for i in range(1,10): #끝값 미포함
    result += i
    
print(result) #45


# 자료형의 인덱스 다 방문시 range()많이 사용
scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.") # 1,2,5 학생
    

#반복문내에서 continue문 만나면 반복문 처음으로 돌아감
scores = [90, 85, 77, 65, 97]
black_list = {2,4} # 2,4번째 학생(85, 65)는 제외하고 싶을 때

for i in range(5):
    if i+1 in black_list: #블랙리스트 번호라면
        continue #로직 안탐
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.") #1, 5 => 2번 학생은 블랙리스트라 스킵
        
#중첩 for문 
#구구단 2~9단
for i in range(2,10): #단
    for j in range(1,10):
        print(i, " x ", j, " = ", i * j)
    print()


