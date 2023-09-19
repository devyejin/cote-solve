import sys
input = sys.stdin.readline

for tc in range(int(input())):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]    # 주어진 단어들로 이루어진 리스트 구성
    is_palindrome = False                           # 회문을 찾았는지 여부를 담아줄 변수

    for i in range(k):                              # 2중 for문을 통해 모든 경우 탐색
        for j in range(k):

            if i == j:                              # 같은 단어를 뽑는 경우는 pass(continue)
                continue

            word = words[i] + words[j]              # 두 단어를 뽑아 붙이기

            if word == word[::-1]:                  # 회문이라면,
                is_palindrome = True                # 찾았다고 표시
                print(word)                         # 출력
                break                               # break(하나만 찾아도 되므로)

        if is_palindrome == True:                   # 회문을 찾았다면 더 찾지 않고 break
            break

    if is_palindrome == False:                      # 회문을 찾지 못했다면 0 출력
        print(0)