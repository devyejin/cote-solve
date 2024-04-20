#range : 순서가 있는 자료형, 연속된 정수 목록을 저장

print(range(1,11)) # 1~10 , range(1, 11)
#꺼내려면 loof돌려야 함

print(range(10,0,-1)) #range(10, 0, -1)

#꺼내는 방법
for i in range(1,11):
    print(i, end=" ") #1 2 3 4 5 6 7 8 9 10 

for i in range(10,0,-1): # 10부터 0(미포함)까지 역순
    print(i, end=" ") #10 9 8 7 6 5 4 3 2 1
    
for i in range(1,11,2): #1부터 11까지(미포함) 2씩 넘으면서
    print(i, end=" ") #1 3 5 7 9 
    
    
# range -> list 형변환
a = range(10) # 0 ~ 9까지 담겨있겠지
b = list(a)
print(b) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]