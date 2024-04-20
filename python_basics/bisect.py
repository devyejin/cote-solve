# bisect 라이브러리를 이용시 -> 이진 탐색 쉽게 구현
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 유용
# bisect_left(a,x) , bisect_right(a,x) => O(logN) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽/오른쪽 인덱스를 찾는 메서드

# 정렬된 리스트 [1,2,4,4,8]이 있을 때, 새로운 데이터 4를 삽입하려 한다 가정
# bisect_left(a,4) => '정렬유지' '가장왼쪽' => idx=2 반환
# bisect_right(a,4) => '정렬유지' '가장오른쪽' => idx = 4 반환

from bisect import bisect_left, bisect_right

a =  [1,2,4,4,8]
x = 4

#새로운 데이터 4를 정렬되도록 넣는데 필요한 인덱스를 찾아라 -> 왼쪽 기준이라면 -> bisect_left idx=2
print(bisect_left(a,4)) # 2
print(bisect_right(a,4)) # 4

# 정렬된 리스트에서 '값이 특정 범위에 속하는 원소의 개수'를 구할 때 유용함 (인덱스로 구간 찾기) => O(logN)
# 값이 left_value, right_value 사이인 데이터이 개수를 반환하는 함수
# 해당 값의 인덱스를 구한 후

def count_by_range(data, left_value, right_value):
    right_index = bisect_left(data,left_value)
    left_index = bisect_right(data,right_value)
    return right_index - left_index # ex 2~4사이의 갯수 = 4-2

#ex
data_list = [1,2,3,3,3,3,4,4,8,9]

#값이 4인 데이터 개수 출력
print(count_by_range(data_list,4,4))