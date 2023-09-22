def solution(my_string):
    answer = []

    for char in my_string:
        if char not in answer:
            answer.append(char)

    return ''.join(answer)


# 좀 더 효율적인 코드
# 리스트 이용도 set이용도 O(n)이지만, set은 검색할 때 O(1)이라 좀 더 빠름
def solution(my_string):
    answer =''
    exclusive_letters = set(my_string) # 중복 제거 O(N)
    for letter in my_string:
        if letter in exclusive_letters: # 들었나 테스트 O(1)
            answer += letter
            exclusive_letters.discard(letter) # 쓴거 제외하기 O(1)

    return answer
