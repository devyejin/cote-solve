mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(mat) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(mat)):
    print(mat[i]) # [1, 2, 3] ...

print(mat[1][1]) # 5


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

# 값을 모두 출력하고 싶을 때

for i in range(3): #3행
    for j in range(4):  #4열
        print(matrix[i][j], end=" ")
        
    print() #한 행 다 작성한 후 개행
'''
1 2 3 4
5 6 7 8
9 0 1 2
'''

# 모든 원소의 합 구하기

result = 0 #초기화

for i in range(3):
    for j in range(4):
        result += matrix[i][j]

print(result) #48


# 델타 탐색 행 인덱스 r(x) , 열 인덱스 c(y)

#상하좌우 델타값
dx= [-1, 1, 0, 0] # dr 
dy= [0, 0, -1, 1] # dc

#델타 값을 가지고 이동시
# 상
nx = x + dx[0]
ny = y + dy[0]

#하
nx = x + dx[1]
ny = y + dy[1]

#좌
nx = x + dx[2]
ny = y + dy[2]

#우
nx = x + dx[3]
ny = y + dy[3]



