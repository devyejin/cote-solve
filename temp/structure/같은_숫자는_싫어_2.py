def solution(arr):
    answer = []
    for num in arr:
        if len(answer) == 0 or answer[-1] != num: # -1인덱스로 마지막 요소 접근 
            answer.append(num)
    return answer
