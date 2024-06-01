from collections import deque

graph = {
      "A" : ["B", "D", "E"]
    , "B" : ["A", "C", "D"]
    , "C" : ["B"]
    , "D" : ["A", "B" ]
    , "E" : ["A"]
}

def bfs(graph, start_vertex):
    visited = []
    queue = deque()
    queue.append(start_vertex)
    
    while queue:
        cur_v = queue.popleft()
        if cur_v not in visited: 
            visited.append(cur_v)
        for destination in graph[cur_v]: 
            if destination not in visited: 
                queue.append(destination)
        
    return visited


print(bfs(graph, "A"))