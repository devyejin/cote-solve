'''
사전 자료형
- key, value 쌍을 데이터로 가지는 자료형
- 리스트, 튜플은 인덱스로 관리되는 반면에, 딕셔너리 자료형은 원하는 데이터를 키로 사용 가능
- ex 사전의 경우 (key, value) (사과, apple) (코코넛,coconut) 이런 식으로 관리가 편함
- 딕셔너리는 내부적으로 '해시 테이블'이용 -> 검색 및 수정 O(1) 시간 복잡도
'''

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
print(data) # {'사과': 'Apple', '바나나': 'Banana'}


'''
* 코테 활용 예시
- 학생 번호가 1 ~ 1e7(천만)까지로 구성되어 있는 상황에서 10,000명의 학생들을 선택했다고 가정.
- 이후 특정한 학생 번호가 주어졌을 때 해당 학생이 선택되었는지 빠르게 알아 내는 방법
  1. 리스트 => 1 ~ 1e7까지의 번호가 '선택되었는지를 저장할 수 있는'리스트를 만들어야 함 -> 천만개의 데이터를 저장할 수 있는 리스트를 만든 후 999만개의 데이터를 미사용 -> 공간 낭비 (다 0으로 해놨다 선택된 idx는 1로 표현한다거나 이건가)
  2. 딕셔너리 => {key:value, ...} 로 저장하면 되기 때문에 만건의 데이터만 넣으면 됨 => 메모리 공간에 효율적
'''

#특정한 원소가 들어있는지 확인 '원소 in 사전' => 리스트, 튜플에서도 사용 가능
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재") #'사과'를 키로 가지는 데이터가 존재
    

#딕셔너리 함수 잘 알기
#키 데이터만 담은 리스트
key_list = data.keys()
print(key_list) # dict_keys(['사과', '바나나', '코코넛'])
print(key_list[1]) #TypeError: 'dict_keys' object is not subscriptable

#값 데이터만 담은 리스트
value_list = data.values()
print(value_list) #dict_values(['Apple', 'Banana', 'Coconut'])
print(value_list[1]) #TypeError: 'dict_values' object is not subscriptable

#각 키에 따른 값 출력
for key in key_list:
    print(data[key])