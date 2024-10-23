mylist = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

#역행렬을 만들고 싶을 때
# mylist = [
#             [1, 4, 7],
#             [2, 5, 8],
#             [3, 6, 9]
#         ]

# 2중 for문으로 i, j를 바꾸는 방법
new_list = [[],[],[]]

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new_list[i].append(mylist[j][i])
        
# zip, unpacking 이용
new_list_sec = list(map(list, zip(*mylist)))
print(new_list_sec)

