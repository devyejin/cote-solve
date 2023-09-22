def solution(s):
    unique_char = {}
    answer = []

    for char in s:
        if char not in unique_char:
            unique_char[char] = 1
        else:
            unique_char[char] += 1

    for key, value in unique_char.items():
        if value == 1:
            answer.append(key)

    return ''.join(sorted(answer))



# 리스트안에 특정 요소가 몇 개 들어있는지 알려주는 메서드 활용한 풀이 방법 list.count(element)
def solution(s):
    letters = list(s)
    answer_list = []

    for letter in letters:
        if letters.count(letter) == 1:
            answer_list.append(letter)

    answer_list.sort()
    answer = ''.join(answer_list)
    
    return answer
