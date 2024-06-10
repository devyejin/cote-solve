import heapq #heapq 모듈 : 파이썬의 리스트를 힙으로 변환하여 사용

graph = {
      1:[(2,2), (1,4)] # (가중치,노드)
    , 2:[(1,3), (9,5), (6,6)]
    , 3:[(4,6)]
    , 4:[(3,3), (5,7)]
    , 5:[(1,8)]
    , 6:[(3,5)]
    , 7:[(7,6), (9,8)]
    , 8:[]
}

def dijkstra(graph, start, final):
    costs = {}
    pq = [] 
    heapq.heappush(pq, (0,start)) # (가중치, 노드)
    
    while pq:
        cur_cost, cur_v = heapq.heappop(pq) # 가중치 값이 낮은게 우선순위가 높음(default)
        
        if cur_v == final:
            return cur_cost
        
        if cur_v not in costs: #idx니까 방문여부 (dict의 not in 연산자는 key 존재 여부)
            costs[cur_v] = cur_cost #방문 기록
            for cost, next_v in graph[cur_v]: #현재 노드가 갈 수 있는 곳 확인
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v)) #방문 예정 
                
    
    return costs[final] #마지막 노드에서의 비용 반환

print(dijkstra(graph, 1, 8))