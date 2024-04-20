#조건문
x = 15
if x >= 10:
    print(x)
    

score = 85

if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif score >= 70:
     print("학점 : c")
else:
     print("학점 : D")
    
score = 85

if score >= 70:
    print('성적이 70점 이상') # 성적이 70점 이상
    if score >= 90:
        print('우수한 성적')
else:
    print('성적이 70점 미만')
    print('조금 더 분발하셈')

print('프로그램 종료') #프로그램 종료


# pass 연산자
# 조건문이 참이더라도 아무것도 처리하고 싶지 않을 때, 디버깅 과정에서 필요한 경우 이용
score = 85

if score >= 80:
    pass #나중에 작성할 소스코드
else:
    print('80미만')

print('프로그램 종료') #프로그램 종료


#간단한 조건문은 한줄로 표시
score = 85

if score >= 80: result = "Success"
else: result = "Fail"

print(result) #Success


#조건부 표현식(Conditional Expression)
score = 85
result = "Success" if score >= 80 else "Fail"

#리스트에 있는 원소의 값을 변경해 또 다른 리스트를 만들 때 유용함
#ex. 리스트에 있는 특정 원소값 제거 한다면
#1.
a = [1,2,3,4,5,5]
remove_set = [3,5]

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result) #[1, 2, 4]

#2. 조건부 표현식 이용
a = [1,2,3,4,5,5]
remove_set = [3,5]

result = [i for i in a if i not in remove_set] # for i in a 먼저 동작! (리스트a에 있는 element for문 돌면서 동작) -> i not in remove_set 각 요소가 remove_set에 없으면 -> 맨 앞 i : result 리스트에 넣음
# [1,2,4]

