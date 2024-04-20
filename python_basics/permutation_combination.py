# itertools : 반복되는 데이터를 처리하는 기능을 가진 라이브러리 => permutation, combination (순열, 조합)
# permutation : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우의 수! (순서o) , 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
from itertools import permutations


data = ['A','B','C']

#data에서 3개를 뽑아 나열하는 모든 경우의 수
result = list(permutations(data, 3))
print(result)