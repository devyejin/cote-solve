# 입력값 1 2 3 4 5 6 을 리스트에 담고 싶을 때
# nums = input() # 문자열로 입력받음

nums = input().split()
print(nums, type(nums)) # ['1', '2', '3', '4', '5', '6'] <class 'list'>

# 문자열 리스트 -> 숫자 리스트로 바꿔야 함!
# 먼저 map을 통해 int로 바꾸고 -> map객체 -> list로
nums__list = list(map(int, input().split()))
print(nums__list, type(nums__list)) # [1, 2, 3, 4, 5, 6] <class 'list'>




# 2차원 리스트 입력받기
nums_matrix = [list(map(int, input().split())) for _ in range(3)]
print(nums_matrix, type(nums_matrix)) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] <class 'list'>