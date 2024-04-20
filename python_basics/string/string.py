#회문 검사하기

word = input()

if word == word[::-1]: #word[::-1] -1 인덱스부터 <- 방향으로 접근
    print('회문입니다')
else:
    print('회문이 아닙니다.')
    
    
#반복문 이용
word = input()

reversed_word =''

for i in word:
    reversed_word = i + reversed_word #글자를 읽어가며 거꾸로 써줘야 하니 i를 앞쪽에!
    
if word == reversed_word:
    print('회문')
else:
    print('회문이 아님')
    

#투포인터
word = input()

left = 0 #시작 인덱스
right = len(word) -1 #마지막 인덱스

is_palindrome = True
while left < right: # 왼쪽->  <-오른쪽 접근이 유지될때까지 반복
    if word[left] == word[right]:
        left += 1
        right -= 1
        continue
    else:
        is_palindrome = False
        break

print(is_palindrome)



#문자열 포함 여부
t = 'hello word'
p = 'wor'

def find_word(p,t): # t에서 p를 찾아라!
    N = len(t)
    M = len(p)
    
    for i in range(N-M+1):
        cnt = 0
        for j in range(M): 
            if t[i+j] == p[j]: # p는 매번 새롭게 돌아야 하니까
                cnt += 1
            else:
                break
            
        if cnt == M:
            return 1
        
    return '못찾았음'

print(find(word(p,t)))