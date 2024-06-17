#입력 0이면 종료


def backtracking(start, curr):
    if len(curr) == 6:
        answer.append(curr[:])

    for i in range(start, len(lst)):
        curr.append(lst[i])
        backtracking(i+1, curr)
        curr.pop()
    
    return answer

while True:
    
    lists = list(map(int, input().split())) 
    if lists[0] == 0:
        break
    
    K = lists[0] #리스트 길이
    lst = lists[1:]
    
    answer = []
    result = backtracking(start=0, curr =[])
    
    for ele in result:
        print(*ele)
    print() #한 줄 띄기