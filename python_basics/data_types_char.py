data = 'Hello World'
print(data)

data = "Dont you know \"Python\"?" # 따옴표 출력하고 싶을 땐 백슬래시 사용
print(data) #Dont you know "Python"?

a = "hello"
b = "world"
print(a+" "+b) # hello world
print(a * 3) # hellohellohello
print((a+" ") * 3) #hello hello hello 

#파이썬의 문자열은 내부적으로 리스트로 처리 즉, 문자열은 여러 개의 문자가 합쳐진 리스트
#리스트의 인덱싱, 슬라이스 사용 가능
a = "ABCDE"
#B부터E까지 얻고 싶을 때
print(a[1:5]) #BCDE
print(a[1:]) #BCDE
print(a[:3]) #ABC

#   0123456789
s = "abcdefghi"
print(s[2:5:2]) #ce
print(s[-6:-1:3]) #dg
print(s[2:5:-1]) # <-순으로 접근할건데 2->5로 갈 수 없으니 []
print(s[5:2:-1]) # <-접근 5부터 2까지 fed
print(s[::-1]) # ihgfedcba <- 문자열 뒤집을 때 많이 사용



#문자열도 리스트이지만, 리스트와 달리 원소 수정/삽입/삭제 불가
word = "python"
word[0] = "j" #'str' object does not support item assignment
print(word)

#문자열을 수정하고 싶다면? -> 진짜 수정은 아니고, 새로운 문자열 객체를 생성 하는 것!
new_word = "j" + word[1:]
print(new_word) #jython
print(word) #python


#문자열 -> 리스트 형 변환 : 문자열을 문자 단위로 쪼개서 넣어줌
a = "python"
b = list(a)
print(b) # ['p', 'y', 't', 'h', 'o', 'n']