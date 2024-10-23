import sys
import heapq
from typing import List, Dict, Tuple
from collections import defaultdict

input = sys.stdin.readline

#상태 그래프
graph = defaultdict(list)
n = int(input()) #노드 수
m = int(input()) #간선 수

for _ in range(m):
    start, end, cost = map(int,input().split())
    graph[start].append((cost, end)) # 우선순위큐 (가중치, 노드)


#n 시작노드 m 도착노드
def minCost(graph:Dict[int, List[Tuple[int, int]]], start:int, end:int) -> int:
    visited = set() #방문 노드 기록
    pq = []
    heapq.heappush(pq, (0, start))  #(가중치, 시작) 
    
    while pq:
        cur_cost, cur_node = heapq.heappop(pq) 
        
        if cur_node in visited:
            continue
        
        visited.add(cur_node) #방문 표시
        
        if cur_node == end:
            return cur_cost
        
        for cost, next_node in graph[cur_node]:
            if next_node not in visited:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_node))
                
    return float('inf')
    
start, end = map(int,input().split())
print(minCost(graph, start, end))