import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville) #정렬 O(n)
    
    while scoville[0] < K: 
        
        if len(scoville) > 1:
            min1 = heapq.heappop(scoville) # O(logn)
            min2 = heapq.heappop(scoville) # O(logn)
            
            new_scovile = min1 + (min2 * 2)
            heapq.heappush(scoville, new_scovile) ## O(logn)
            answer += 1
        else: # 0번째가 k미만이고, 길이도 1이하라면 불가능하니
            return -1
    return answer    
#시간 복잡도 while문 도니까 O(n log n)