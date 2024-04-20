# 광산에서 10개의 광물을 채굴, 각 등급
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

#광물들 중 1등급 광물이 존재하는가?
#sol1
if 1 in gems:
    print(True)
else:
    print(False)

#sol2 - flag이용
grade1 = False # 1등급이 존재하면 grade1 True기록

for i in gems:
    if i == 1:
        grade1 = True
        break #효율화

print(grade1)



#1,2,3 등급 광물이 각각 몇 개 있는지 기록
grades = {1:0, 2:0, 3:0} #초기화

for i in gems:
    grades[i] += 1 #딕셔너리는 key로 접근

print(grades) # {1: 2, 2: 3, 3: 5}


#광물 등급의 합 < 15 : 성공,  < 23 : 보통, 30 > 초과 => 올해의 성공 척도 출력
result = sum(gems)

if result <= 15:
    print('성공')
elif result <= 23:
    print('보통')
else:
    print('실패')
    

# max, min 직접 구현
nums = [7, 1, 2, 4, 6, 8, 3]

#최댓값
max_num = -1 #작은 수로 초기화
for num in nums:
    if max_num < num:
        max_num = num

print(max_num) # 8

#최솟값
min_num = 9999 #큰 수로 초기화
for num in nums:
    if min_num > num:
        min_num = num

print(min_num) # 1

# -> 리스트를 다 순회해야 하니 O(N)
# 내장 함수 max(), min()은 최적화되어 있어 O(1)
