from collections import deque

def solution(arr):
    arr = deque(arr)
    trans_arr = []
    
    #현재값과 이전값을 비교
    prev = None
    
    while arr:
        current = arr.popleft()
        
        if prev is None or current != prev: #첫 번째 요소인 경우 or prev랑 다른 경우
            trans_arr.append(current)
        
        prev = current
        
    return trans_arr