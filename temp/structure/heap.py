import heapq #힙큐 모듈 : 리스트를 힙으로 변환

priortiy_queue = [] #리스트를 힙으로 사용

#요소 추가 (우선 순위, 값) 튜플 형태로 추가
heapq.heappush(priortiy_queue, (1, 'Task 1'))
heapq.heappush(priortiy_queue, (4, 'Task 4'))
heapq.heappush(priortiy_queue, (3, 'Task 3'))
heapq.heappush(priortiy_queue, (2, 'Task 2'))

print("우선 순위 큐 : ", priortiy_queue) # 우선 순위 큐 :  [(1, 'Task 1'), (2, 'Task 2'), (3, 'Task 3'), (4, 'Task 4')]

#우선순위가 가장 높은 요소 추출 heappop() , deault : 숫자가 작은 경우
print(heapq.heappop(priortiy_queue)) # (1, 'Task 1')
print("pop 후 : ", priortiy_queue) # pop 후 :  [(2, 'Task 2'), (4, 'Task 4'), (3, 'Task 3')]
