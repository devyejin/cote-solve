graph = {
      "A" : ["B", "D", "E"]
    , "B" : ["A", "C", "D"]
    , "C" : ["B"]
    , "D" : ["A", "B" ]
    , "E" : ["A"]
}

def dfs(graph, cur_v):
    visited = []
    visited.append(cur_v)
    for destination in graph[cur_v]:
        if destination not in visited
        dfs( )