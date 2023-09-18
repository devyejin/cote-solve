
n = int(input())

for _ in range(n):
    idx, word = input().split() #한 번에 쪼개 받는것도 포인트
    idx = int(idx)

    print(word[:idx-1] + word[idx:]) #인덱스 기준으로 잘라서 이어붙이기
