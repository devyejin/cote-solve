import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]) )
        # print(days)
        
    while days:
        current = days.popleft()
        count = 1
        
        while days and days[0] <= current: #idx갱신되니까
            days.popleft()
            count += 1

        answer.append(count)
    
    return answer


progresses = [93, 30, 55]	
speeds = [1, 30, 5]	
print(solution(progresses, speeds))