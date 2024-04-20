def add(a,b):
    return a+b

print(add(3,7)) #10



def add(a,b):
    print('함수의 결과 : ', a+b)
    
add(1,1) #함수의 결과 :  2

add(b=10, a=1) #인자를 지정해서 값을 넣어줄 수 있음


#함수 안에서 함수 박의 변수 데이터를 변경해야 하는 경우 -> global 변수를 지정 => 함수 안에서의 지역 변수를 만들지 않고, 밖의 전역 변수를 참조하게 됨
a = 0 #전역 변수

def func():
    global a
    a += 1
    
for i in range(10):
    func()
    
print(a) # 10


#람다 표현식 -> 간단한 삼수 정의 유용
print((lambda a, b: a+b)(3,7))  #lambda 변수 : return