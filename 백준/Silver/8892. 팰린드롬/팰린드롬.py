import sys
input = sys.stdin.readline   # 내장함수 input()은 사용자 입력 기다림, sys.stdin.readline은 바로읽음(파일입력시 많이 사용)


for tc in range(int(input())):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]
    is_pal = False

    for i in range(k):

        if is_pal == True:
            break

        for j in range(k):

            if i == j:
                continue

            word = words[i] + words[j]

            if word == word[::-1]:
                is_pal = True
                print(word)
                break

    if is_pal ==False:
        print(0)