
def solution(n):
    
    str_n = str(n)
    
    reversed_list = list(map(int,reversed(str_n)))
    
    return reversed_list

# 다른사람 풀이
# 꼭 함수명이 solution일 필요 없음, 간결하게 한 줄로 
def digit_reverse(n):
    return list(map(int,reversed(str(n))))

#
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]  #숫자 배열로 만든다음 뒤집기
