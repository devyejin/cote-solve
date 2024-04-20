#표준 라이브러리 : 자주 사용되는 표준 소스코드를 미리 구현해놓은 라이브러리
# 내장 함수, itertools, heapq(힙 기능, 우선순위 큐 기능 구현시 사용), bisect (이진 탐색 기능) , collections (덱, 카운터 자료구조), math (팩토리얼, 제곱근, 최대공약수 등)


print(sum([1,3,5,4])) #sum() : 리스트와같은 iterable객체가 입력으로 주어지면 모든 원소의 합 구해줌
print(min(6,23,2))
print(max(6,23,2))

#eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
print(eval("(3+5) * 8")) #64

#sorted() : iterable객체 정렬, key속성으로 정렬 기준 명시 가능, reverse 속성으로 역순

data = [9,1,8,5,4]
print(sorted(data)) #[1, 4, 5, 8, 9] 오름차순 정렬,
print(data) # [9, 1, 8, 5, 4] : sorted()의 경우 원본에 영향 X 객체.sort() 이렇게 접근하는 메서드가 원본에 영향 ex. list.sort()
print(sorted(data, reverse=True)) #내림차순 [9, 8, 5, 4, 1]

data = [('홍길동',35), ('이순신',75), ('어무개', 50)] #튜플의 두번째 원소(idx=1)를 기준으로 정렬하고 싶을 때  lambda 인자 : 표현식
result = sorted(data, key= lambda x : x[1], reverse=True)
print(result) # [('이순신', 75), ('어무개', 50), ('홍길동', 35)]


# list와 같은 iterable객체는 sort() 메서드를 내장하고 있음, sort() 메서드의 경우, 리스트 객체의 내부 값이 변경됨
data = [9,1,8,5,4]
print(data.sort()) # none => list.sort() 내부값이 정렬되는거지 반환x
print(data) # [1, 4, 5, 8, 9]