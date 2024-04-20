'''
입출력
- input() : 한 줄의 '문자열'을 입력받음
- 65 90 30 ... 이런식으로 공백으로 데이터가 구분되는 경우가 많음
- list(map(int, input().split())) 을 이용 => input()으로 입력받은 데이터를 split()을 이용해 공백으로 나눈 리스트로 받음 map을 이용하여 해당 모든 원소들에 int() 적용
5 #데이터 개수
65 90 75 34 99
'''
import sys

n = int(input())
data = list(map(int,input().split()))

print(data) # [65, 90, 75, 34, 99]

#내림차순 정렬
data.sort(reverse=True)
print(data) # [99, 90, 75, 65, 34]


#많은 데이터 입력 받아야 할 때는 sys라이브러리 사용
# import sys
data = sys.stdin.readline().rstrip() # readline() 한 줄 입력 받고 rstrip() 함수를 꼭 호출! 엔터제거!
print(data)


# 출력
answer = 8
print("정답은" + answer + "입니다.") #error 문자형끼리만 + 연산 가능 TypeError: can only concatenate str (not "int") to str
print("정답은" + str(answer) + "입니다.") #정답은8입니다.
print(f"정답은 {answer} 입니다.") #f-string문법 사용시 자료형 변환 안해도 됨!


#f-string
name = "kyle"
age = 20

print(f"이름의 길이는 {len(name)} 입니다.") #이름의 길이는 4 입니다.
print(f"내년이 되면 {age + 1}살이 됩니다.") #내년이 되면 21살이 됩니다.