

def solution(absolutes, signs):
    sum = 0
    
    for _ in range(len(absolutes)):
        sign = 1
        
        if signs.pop() == False:
            sign = -1
            
        sum += (absolutes.pop() * sign)

    return sum


# 다른 풀이 (컴프리헨션)

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
