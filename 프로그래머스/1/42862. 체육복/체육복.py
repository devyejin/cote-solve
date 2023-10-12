def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n+2)
    
    for i in lost:
        students[i] -= 1
    
    for j in reserve:
        students[j] += 1
    
    for k in range(n+2):
        if students[k] == 2:
            
            if students[k-1] == 0:
                students[k-1] += 1
                students[k] -= 1
            
            elif students[k+1] == 0:
                students[k+1] += 1
                students[k] -= 1
        
    answer = n - students.count(0)
    
    
    return answer