'''
모듈 : 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 모듈을 이용하면 다른 파이썬 파일(.py)에 작성된 기능을 가져다 사용 가능
- 재사용, 유지보수 편리
- 모듈은 import 키워드로 불러다 사용

- 파이썬에서 제공하는 라이브러리가 모듈의 집합임
'''
# random 모듈
import random

number = random.randint(1,5) # 1~5중 무작위로 1개 택
print(number) #3

numbers = [10,20,30,40,50]
number = random.choice(numbers) #리스트에서 무작위로 하나 택
print(number)

#... 