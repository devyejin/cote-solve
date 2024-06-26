def solution(prices):
    n = len(prices)
    answer = [-1] * n
    stack = []
    #현재 가격을 기준으로 과거 가격 바라보기
    #prices =[1, 2, 3, 2, 3]
    #stack = [] : 상승 상태인 idx
    for current in range(n):
        #stack의 값들과 비교
        while stack and  prices[current] < prices[stack[-1]] : #하락이라면 시간 구하기
            past = stack.pop()
            answer[past] = current - past
        #끝까지 돌고 나면 마지막 idx값을 stack에 추가
        stack.append(current)
    
    print(stack)    
    #stack에 남은 idx들은 계속 상승인 값들이니까, 시간 별도로 구하기
    for idx in stack:
        answer[idx] = n - idx - 1
    return answer
