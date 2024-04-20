#heapq :  heap 기능을 위한 라이브러리
# 다익스트라 최단 경로, 우선순위 큐 등에 사용
# 파이썬은 최소 힙(min heap)으로 구성되어 단순히 원소를 힙에 넣고 빼는것만으로도 O(NlogN)에 오름차순 정렬이 됨
# 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은 원소'

# 원소 삽입 : heapq.heappush(), 원소 뺄 때 : heapq.heappop()
# 힙 정렬 예제
# idea) 임시 h에 heapq(최소힙)을 이용해서 넣음 -> 최소 원소가 상단에 위치하니까, 꺼내서 result에 넣을때도 가장 작은 값 부터 들어가게 됨!
import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value) #하나씩 넣기
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)): #자료구조 크기만큼 돌기
        result.append(heapq.heappop(h)) #하나씩 꺼내기
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# => heapq의 경우 최소 힙이기 때문에 '힙에 값을 추가할 때마다 최소 값을 루트에 위치시킴!' 
# => 힙에서 값을 추출하면 가장 작은 값부터 추출



# 파이썬은 최대 힙을 제공하지 않음
# 최대값부터 꺼내고 싶다면, 모든 원소에 음수를 붙여서 최소힙을 구한 다음 부호 변경!
# idea) 최대값순으로 하고 싶은거니까, 임시 h (heapq)에 -value로 넣음 => -9 -8 ... 이런식으로 들어갔겠지 => 꺼낼때 -9 -8 이런식으로 나오니까 꺼내진 값에 음수부호 붙여서 result에 담아버림

def heapsortmax(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value) #부호 반대로!
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 꺼내진 값 heapq.heappop(h) 에 음수부호 붙인 다음 result(결과 리스트)에 넣어버리기
    return result

result = heapsortmax([6,3,6,5,3,2,1])
print(result) # [6, 6, 5, 3, 3, 2, 1]