

N = int(input())

words = [input() for _ in range(N)]
words = list(set(words)) # set이용해서 중복 제거

words.sort() # 사전순 정렬(오름차순이 기본)
words.sort(key= lambda x : len(x)) # (오름차순이 기본이니까 짧은 순이겠지)

for word in words:
    print(word)



# 출력 다른 방법
while words:
    print(words.pop(0))                         
