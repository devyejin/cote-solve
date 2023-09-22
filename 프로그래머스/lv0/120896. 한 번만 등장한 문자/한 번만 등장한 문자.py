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