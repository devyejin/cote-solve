def solution(my_string):
    answer = ''
    
    for char in my_string:
        if char not in answer:
            answer += char
            
    return answer


#좀 더 효율적인 풀이법
#     딕셔너리의 key가 중복허용되지 않는점을 이용한 후 join으로 문자열 반환
#    return ''.join(dict.fromkeys(my_string))
