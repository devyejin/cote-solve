# 1~10 정수 중 홀수만 출력
for i in range(1,11,2):
    print(i, end=" ") # 1 3 5 7 9 

#특정 횟수만큼 코드 반복
for i in range(3):
    print("이 코드를 3번 반복")

#응용
numbers = [1,2,3,4,5]

for i in range(len(numbers)):
    print(numbers[i])

for index, value in enumerate(numbers):
    print(f"Index : {index}, Value : {value}")
    

numbers = [10, 20, 30, 40, 50]
i = 0 #초기화

while i < len(numbers): #조건
    print(numbers[i])
    i += 1 #증감식
    
#응용) 리스트가 빌 때까지 삭제하면서, 그 삭제한 원소를 출력
# 리스트에 원소가 1개 이상이면 True, 없으면 False 판별 이용

numbers = [1, 2, 3, 4, 5]

while numbers: # 리스트가 비면 False판별 -> while문 종료
    deleted_number = numbers.pop() #리스트 뒤쪽부터 pop
    print(deleted_number)
    # print(numbers)

print(numbers) #다 끝났으니 빈 리스트 []

#조건문에 들어가는 변수는 반드시 초기화 해야 함!
#그래서 위에서 증감식에 사용하는 i를 반복문 밖에서 초기화 해줬던 것


# break -> 반복문 종료, continue -> 다음 반복문으로 이동(필터링)
numbers = [1, 2, 3, 4, 5]
