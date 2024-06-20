import heapq

def solution(sequence, k):
    answer = []
    e = 0
    interval_sum = 0
    temp = []
        
    for s in range(len(sequence)):
        while e < len(sequence) and interval_sum < k:
            interval_sum += sequence[e]
            e += 1
        if interval_sum == k:
            heapq.heappush(temp, (e-s, [s, e-1]))
            #   temp.append({e-s, [s,e]}) #key 값으로 거리값을 저장         
        interval_sum -= sequence[s]
    
    if temp:
        smallest_interval = heapq.heappop(temp)
        answer = smallest_interval[1]
        
    return answer

