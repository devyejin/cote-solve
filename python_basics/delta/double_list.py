# 2차원 리스트 + 순회 -> 완탐 

matrix = [[3, 7, 9],
        [4, 2, 6],
        [8, 1, 5]]

trails = [] #순회 궤적 담을 리스트

for r in range(3): #행
    for c in range(3): #열
        trails.append(matrix[r][c])
        
#완탐 궤적 출력
print(trails) # [3, 7, 9, 4, 2, 6, 8, 1, 5]




#행은 순회, 열은 역순행으로 완탐 ex. 9 7 3 6 2 4 ...
#range(start, stop, step)
trails = []

for r in range(3):
    # 2 -> 1 -> 0 반복
    for c in range(2, -1, -1):
        trails.append(matrix[r][c]) # [9, 7, 3, 6, 2, 4, 5, 1, 8]

print(trails)



#행 순회, 열은 교차 즉, -> <- -> 
# 행 짝 ->, 행 홀 <-
trails = []

for r in range(3):
    if r % 2 == 0:
        for c in range(3):
            trails.append(matrix[r][c])
    else:
        for c in range(2, -1, -1):
            trails.append(matrix[r][c])

print(trails) # [3, 7, 9, 6, 2, 4, 8, 1, 5]



# 열 우선 순회 1행 -> 2행 -> 3행
# 00 10 20 10 11 21 ..

trails = []

for c in range(3):
    for r in range(3):
        trails.append(matrix[r][c])

print(trails) # [3, 4, 8, 7, 2, 1, 9, 6, 5]

#아니면 00 01 02 10 11 21 20 21 22
#       00 10 20 10 11 12        => 요 꼬라지니까
for r in range(3):
    for c in range(3):
        trails.append(matrix[c][r]) #이렇게 순서 바꿔줘도 ㅇㅋ
        
x = 3 
y = 6 # 서로 바꾸고 싶을 떄
x , y = y, x        
print(x,y) # 6 3



#전치
for r in range(3):
    for c in range(3):
        if r > c:
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
print(matrix)

#[[3, 4, 8],
# [7, 2, 1],
# [9, 6, 5]]


#전치 zip 이용 => zip하면 원소가 튜플이 됨
# zip : 세로로 찝고, 튜플로 반환 즉 (3,7,9) (4,2,6)
zip_matrix = zip(*matrix)
# print(zip_matrix) <zip object at 0x000001F8CDBFB9C0>

zipeed_matrix = list(zip(*matrix))
print(zipeed_matrix) # [(3, 7, 9), (4, 2, 6), (8, 1, 5)]


#튜플 : read-only, 데이터 수정 필요시 map 함수를 이용해서 list로 변환!
traspo_list = list(map(list, zipeed_matrix)) 
print(traspo_list) # [[3, 7, 9], [4, 2, 6], [8, 1, 5]]


# * 기호 : 이중 리스트로 감싸졌을 때, outer list 벗기는 용도

print(*matrix) # [3, 4, 8] [7, 2, 1] [9, 6, 5]




#오른쪽 90도 회전
matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]

n = 3

rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[n-j-1][i]

print(rotated_matrix) # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]





#왼쪽으로 90도 회전
matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]

n = len(matrix)


rotated_matrix = [[0] * n for _ in range(n)]

for i in range(3):
    for j in range(3):
        rotated_matrix[i][j] = matrix[j][n-i-1]
    
print(rotated_matrix) # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
        

#zip 이용하면 더 간단
