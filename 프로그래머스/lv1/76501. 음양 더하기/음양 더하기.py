

def solution(absolutes, signs):
    sum = 0
    
    for _ in range(len(absolutes)):
        sign = 1
        
        if signs.pop() == False:
            sign = -1
            
        sum += (absolutes.pop() * sign)

    return sum

