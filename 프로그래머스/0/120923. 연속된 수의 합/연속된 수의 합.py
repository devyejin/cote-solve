def solution(num, total):
    
    f = 0
    # total == num * f + (num - 1) * num / 2
    f = (total - (num -1) * num / 2) / num
    # print(f) # f시작 값, 나눗셈때문에 실수 됨 
    f = int(f)
    
    answer = [f+i for i in range(num)]
    return answer
