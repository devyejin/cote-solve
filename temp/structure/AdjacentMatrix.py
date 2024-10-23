from collections import deque
#그래프를 구현 (인접 행렬 / 인접 리스트 / 암시적 그래프 )
graph = {
      "A" : ["B"]
    , "B" : ["C", "E"]
    , "C" : ["B", "D" ]
    , "E" : ["B", "D", "F"]
    , "D" : ["C", "D", "F"]
    , "F" : ["D", "E"]
}

def bfs(graph, start_v):
  visited = [start_v]
  queue = deque(start_v)
  while queue:
    cur_v = queue.popleft()
    for v in graph[cur_v]: #현재 노드가 갈 수 있는곳들 체크
      if v not in visited: #방문을 안한 곳이라면
        visited.append(v)
        queue.append(v) #queue에 넣기(v가 갈 수 있는 곳 확인)
  return visited

print(bfs(graph, "A"))

def bfs2(graph, start_v):
  queue = deque(start_v) #시작점 queue에 넣고 시작
  visited = [] #방문 기록용
  
  while queue:
    cur_v = queue.popleft() # queue.pop(0)
    if cur_v not in visited: #방문안했으면
      visited.append(cur_v) #방문 기록
      
      #갈 수 있는 곳들 queue에 넣기 -> 종료
    for destination in graph[cur_v]:
      if destination not in visited:
        queue.append(destination)
  
  return visited

print(bfs2(graph, "A"))
