'''
collections 라이브러리 -> 다양한 자료구조 제공 그 중 deque, counter 알아두기!

* deque
- 파이썬은 deque를 이용해서 que 구현

- 리스트 자료형은 append(), pop() 메서드로 데이터를 추가/삭제 하는데 '가장 뒤쪽 원소'를 기준으로 수행
- 앞쪽에 있는 원소를 처리할 때 리스트에 포함된 데이터가 많을 수록 많은 시간이 소요됨 
- 앞쪽에 원소를 추가/제거시 O(N)
- 가장 앞쪽에 원소 추가, 제거 -> 리스트 : O(N) / deque : O(1)
- 가장 뒤쪽에 원소 추가, 제거 -> 리스트 : O(1) / deque : O(1)

- deque는 리스트와 달리 인덱싱, 슬라이싱 기능 사용 불가
- 연속적으로 나열된 데이터의 시작 / 끝 부분에 데이터 삽입/삭제시 효과적
- stack, que 기능을 모두 포함해 stack, que 자료구조 대용으로 사용 가능

- 첫번째 원소 제거/추가 popleft(), appendleft(x) 
- 끝에 원소 제거/추가 pop(), append(x)
'''

#리스트 [2,3,4]의 가장 앞쪽, 뒤쪽에 원소 삽입 
from collections import deque

data = deque([2,3,4])
#가장 앞에 1, 맨 뒤에 5 삽입
data.appendleft(1)
data.append(5)

print(data) # deque([1, 2, 3, 4, 5])
print(list(data)) #리스트 자료형으로 변환 [1, 2, 3, 4, 5]



#Counter 는 등장 횟수를 세능 기능
#ex. iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) #3
print(counter['red']) #2
print(counter) # Counter({'blue': 3, 'red': 2, 'green': 1})
print(dict(counter)) #딕셔너리 자료형으로 변환 => {'red': 2, 'blue': 3, 'green': 1}


#math 라이브러리
import math

print(math.factorial(5)) #5! 120
print(math.sqrt(7)) 
print(math.gcd(21,14)) #최대공약수 7
print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045