import heapq
from collections import deque

def solution(priorities, location):
    answer = 0
    
    dq = deque([(prioritiy, idx) for idx, prioritiy in enumerate(priorities)])
    
    while dq:
        current = dq.popleft()
        
        if any(current[0] < item[0] for item in dq):
            dq.append(current) #낮으면 다시 넣기
        else:
            answer += 1
            
            if current[1] == location:
                return answer