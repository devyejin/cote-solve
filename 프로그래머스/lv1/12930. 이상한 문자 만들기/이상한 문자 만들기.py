def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1] #마지막 단어에서도 ' ' 공백이 붙어버려서 제거하고 출력


# 기존 풀이인데, 이 방식은 테스트케이스 일부가 통과 못함
# 제한사항에! 문자열 전체의 인덱스가 아닌 !!단어별 인덱스!!
def solution(s):
    count = 1
    answer = []
    for char in s:

        if count % 2 == 1:
            answer.append(char.upper())
        else:
            answer.append(char.lower())

        count += 1 ## 파이썬은 count++ 미지원

    return ''.join(answer) # 리스트를 문자열로 반환하는 방법

