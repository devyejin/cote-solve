import heapq
from collections import defaultdict
from typing import List #타입 힌팅을 위해 사용

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
            graph = defaultdict(list) 
            for time in times:
                graph[time[0]].append((time[2], time[1])) #(가중치, 노드) 우선순위큐
            
            costs = {}
            pq = [] 
            heapq.heappush(pq, (0, k)) #(가중치, 시작)
            
            while pq:
                cur_cost, cur_node = heapq.heappop(pq)    
                if cur_node not in costs:
                    costs[cur_node] = cur_cost
                    for cost, next_node in graph[cur_node]:
                        next_cost = cur_cost + cost
                        heapq.heappush(pq, (next_cost, next_node))
                        
            for node in range(1, n+1):
                if node not in costs:
                    return -1
            
            return max(costs.values())