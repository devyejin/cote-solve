#내장 함수 sorted(), reversed() => 기존 데이터에 영향X
#정렬
a = [3, 1, 0, 5, 31]

print(sorted(a)) #오름차순 [0, 1, 3, 5, 31]
print(sorted(a, reverse=True)) # [31, 5, 3, 1, 0]
print(a) #기존 리스트에 영향X [3, 1, 0, 5, 31]

#리스트 값 뒤집기
print(reversed(a)) # <list_reverseiterator object at 0x000001D2596B7250>
print(list(reversed(a))) # [31, 5, 0, 1, 3] 형변환 해줘야 함
print(a) # [3, 1, 0, 5, 31]

# 번외)
print(a[::-1]) # [31, 5, 0, 1, 3]


#리스트 내장 메서드 => 기존 리스트에 영향 O

#끝에 원소 추가 O(1)
a = [1, 2, 3, 4, 5]
a.append(6)

print(a) #[1, 2, 3, 4, 5, 6]

#특정 idx=i에 원소 x삽입 O(N)
a = [1, 2, 3, 4, 5]
a.insert(1,10)
print(a) #[1, 10, 2, 3, 4, 5]

#끝에 원소 삭제 후 반환 O(1)
a = [1, 2, 3, 4, 5]
b = a.pop()
print(a) #[1, 2, 3, 4]
print(b) #5

#특정 idx= i번째 원소 삭제 후 반환 O(N)
a = [1, 2, 3, 4, 5]
b = a.pop(3)
print(a) #[1, 2, 3, 5]
print(b) #4

#특정 원소 중 첫 번째 값 제거, 반환X
a = [1, 2, 3, 4, 3, 5, 3]
a.remove(3)
print(a) # [1, 2, 4, 3, 5, 3]

#리스트 정렬 => 내장 메서드니까 기존 리스트에 영향 o
a = [3, 5, 1, 4, 2]
a.sort() #오름
print(a) # [1, 2, 3, 4, 5]

a.sort(reverse=True) #내림
print(a) # [5, 4, 3, 2, 1]

# 내장 함수 sorted() vs 리스트 내장 메서드 sort()
# 내장 함수의경우 인자로 받은 리스트를 정렬한 후 새로운 리스트 반환
# 내장 메서드는 원본 자체를 정렬! 반환값이 없음

#리스트 뒤집기
a = [3, 5, 1, 4, 2]
a.reverse()
print(a) # [2, 4, 1, 5, 3]

#리스트 확장 extend() vs append() 주의깊게 보기!
a = [1, 2, 3, 4, 5]
a.extend([6,7,8]) # [6,7,8] 원소가 분해되어 A 끝에 붙음
print(a) # [1, 2, 3, 4, 5, 6, 7, 8]

a.append([10,11,12]) # [1, 2, 3, 4, 5, 6, 7, 8, [10, 11, 12]]
print(a)

a.append(12)
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, [10, 11, 12], 12]


# 리스트에 들어있는 원소의 개수
print(a.count(12)) # 1
print(a.count([12])) # 0
print(a.count([10,11,12])) # 1

#원소x가 처음 등장하는 인덱스
a = [3, 5, 1, 4, 2, 5]
print(a.index(5)) #1
print(a.index(10)) # 원소x가 리스트에 없으면 에러 발생 ValueError: 10 is not in list


#문자열 메서드
#split(기준 문자) :  기준 문자를 기준으로 나눠 리스트로 반환, 기존 문자열 객체는 유지
s = "kyle,alex,justin,ken"
print(s.split(",")) # ['kyle', 'alex', 'justin', 'ken']
print(s) # kyle,alex,justin,ken

s = "I play the piano"
print(s.split(" ")) # ['I', 'play', 'the', 'piano']

#문자열 왼쪽, 오른쪽에서 특정 문자를 제거 -> 새로운 문자열 반환, 기존 문자열 유지
s = "aHello Worlda"
print(s.strip("a")) # Hello World
print(s) # aHello Worlda

#기본값은 공백
s = " Hello World "
print(s.strip()) #Hello World <- 양쪽 공백 제거

#제거할 문자 여러개 넣으면.... => 해당 문자들을 양쪽에서 모두 제거하고 새로운 문자열 반환
s = "Hello World"
print(s.strip("Hd"))  #ello Worl

s = "Hello World"
print(s.strip("He")) # llo World

s = "Hello World"
print(s.strip("hod")) #Hello Worl


#찾는 문자가 처음으로 나타나는 인덱스 반환 find() vs index()
s = "python"

print(s.find("t")) #2

#없으면 -1 반환
print(s.find("j")) # -1


print(s.index("t")) #2
print(s.index("j")) #index()의 경우 error 반환  ValueError: substring not found

#특정 문자의 개수 반환
s = "hello python"
print(s.count("l")) #2
print(s.count("py")) #1

s = "banana"
print(s.count("na")) #2


#기존 문자를 새로운 문자열로 치환한 새로운 문자열 반환(기존 문자열 유지)
s = "I play the piano"
print(s.replace("piano", "violin")) #I play the violin

s = "python"
print(s.replace("p", "")) #ython
print(s.replace("p", " ")) # ython (공백도 자리 차지)


#삽입할문자.join(리스트) : 리스트 원소들 사이에 특정 문자 삽입한 새로운 문자열 반환

words = ["I", "play", "the", "piano"]
print("$".join(words)) #I$play$the$piano

words = ["I", "play", "the", "piano"]
print(" ".join(words)) #I play the piano

words = ["a", "p", "p", "l", "e"]
print("".join(words)) #apple

#리스트의 모든 element가 문자가 아니면 error
numbers = [1, 2, "3", "4", "5"]
print("".join(numbers)) # TypeError: sequence item 0: expected str instance, int found