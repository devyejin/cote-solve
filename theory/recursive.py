'''
* recursive function : 함수 내에서 동일한 함수 재호출
- 특정 조건이 되면 재귀함수 호출이 멈춰야 함
- 재귀함수 vs 반복문
  재귀함수는 반복문으로 구현 가능
  재귀함수가 코드는 간결하지만 -> 메모리, 시간 측면에서 비용이 큼 (아닌 경우가 존재 -> 이떄 재귀로 풀이)
  재귀호출은 비효율적임 ex. 피보나치수열 호출시 스택 쌓이는거 생각해보면(직접 그려봄 ㅋ)

- 재귀를 알아야 하는 이유 -> 분할정복, 다이나믹 프로그래밍의 기본
  -> 반복문보다는 비효율적이지만, 코드가 간결하고 가독성이 높음

- 재귀의 핵심 1. 문제의 정의를 정확히 표현, 2. 종료 조건 (피보나치의 경우 f(n) = f(n-1) + f(n-2) ,  n == 1이면 종료)

- 선언형 프로그램 : 목표를 명시하고, 알고리즘을 명시하지 않는 것(중간 풀이는 컴퓨터가 알아서!)
'''

def recur(depth):
    if depth == 3: #종료 조건
        return
    
    print(f"현재 {depth}에 있습니다.")
    
    recur(depth+1)
    print(f"{depth}에 있을 때 아직 실행이 안되고 스택에 쌓였던 실행문")

recur(0)

#스택 이해
def recur2(floor):
    if floor == 0:
        return
    
    print(f"현재 floor는 {floor}")
    recur2(floor-1)
    print(f"{floor}에 있을 때 미실행 라인")
    
recur2(4)

#피보나치 수 구하기 
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4)) #3
print(fibo(5)) #5

#피보나치 수 구하는 과정을 재귀를 사용하면 중복 연산이 발생 => O(2^n)


#다이나믹 프로그래밍 ( 큰 문제를 작은 문제로 나누기, 작은 문제에서 해결한 답이 큰 문제에서도 동일) - 메모이제이션 기법 => O(N)
d = [0] * 100 #계산된 결과 저장할 리스트

def fibo_memo(x):
    if x == 2 or x == 1: #종료 조건
        return 1
    
    #이미 계산된 적 있는 문제라면 재사용
    if d[x] != 0:
        return d[x]
    #아직 계산한 적 없으면 재귀로 계산
    d[x] = fibo_memo(x-1) + fibo_memo(x-2)
    return d[x]


print(fibo_memo(5)) #5
print(fibo_memo(99)) # 218922995834555169026



#메모이제이션(다이나믹 프로그래밍) 호출되는 함수 확인
d = [0] * 100

def fibo_memo_show(x):
    print('f('+str(x)+')', end=' ')
    if x == 1 or x == 2: #종료 조건
        return 1
    if d[x] != 0: #캐싱된 값이 있다면
        return d[x]
    #캐싱된 값이 없다면
    d[x] = fibo_memo_show(x-1) + fibo_memo_show(x-2)
    return d[x]

print(fibo_memo_show(6)) # f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4) 8


#반복문으로 푸는 경우
d = [0] * 100 #캐싱을 위한 리스트

d[1] = 1
d[2] = 1
n = 99 

#f(n-2) + f(n-1) = f(n) 이걸 밑에서부터 쌓아 가기 => n번 도니까 O(n)
for i in range(3, n+1): # 3부터 n까지 만들기
    d[i] = d[i-1] + d[i-2]


print(d[n]) # 218922995834555169026


#하노이 탑
# 최종목적지 최하단에 가장 큰 원반이 있어야 함

#종료 조건을 잘 설정할 것
#문제의 정의를 선언하는 부분을 잘 읽을 것(피보나치처럼!)
#- N개의 원반을 옮기기 위해서는 N-1개의 원반을 이웃한 기둥으로 옮겨야 함
#- 가장 큰 원반이 최종 목적 기둥으로 옮겨야 함
#- 이제 이웃한 기둥에서 N-1개의 원반을 최종 목적 기둥으로 옮겨야 함

#종료조건 = start_peg에 원반이 하나 남았을 때 end_pag로 옮기고 끝난다

# def move_disk(disk_num, start_peg, end_peg):
#     print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" %(disk_num, start_peg, end_peg))

# def hanoi(num_disks, start_peg, end_pag):
#     hanoi_sub(num_disks, start_peg, end_pag,2)

# def hanoi_sub(N, start_peg, end_peg, other_peg):
#     if N == 1: # 원반이 한개인 경우
#         move_disk(1, start_peg, end_peg) #한개의 원반을 시작기둥에서 끝기둥으로 옮기고 종료
#     else:
#         hanoi_sub(N-1, start_peg, other_peg, end_peg)
#         move_disk(N, start_peg, end_peg)
#         hanoi_sub(N-1, other_peg, end_peg, start_peg)



# # 테스트 코드 (원반의 갯수, 시작 기둥, 종료 기둥)
# hanoi(3,1,3) #3개의 원반을 1번 기둥에서 3번 기둥으로 옮겨라


def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" %(disk_num, start_peg, end_peg))


def hanoi(n_disks, start_peg, end_peg):
    hanoi_sub(n_disks, start_peg, end_peg, 2) #2는 보조_peg 번호
    
def hanoi_sub(n, start_peg, end_peg, sub_peg):
    if n == 1: #시작 -> 끝
        move_disk(1, start_peg, end_peg)
        return
    else:
        hanoi_sub(n - 1, start_peg, sub_peg, end_peg)
        move_disk(n, start_peg, end_peg)
        hanoi_sub(n - 1, sub_peg, end_peg, start_peg)

hanoi(3,1,3)
