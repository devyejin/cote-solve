from collections import deque

def solution(priorities, location):
    answer = 0
    
    dq =  deque([(priority, idx) for idx, priority in enumerate(priorities)])
    
    while dq:
        current = dq.popleft()
        if any(current[0] < item[0] for item in dq):
            dq.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer
