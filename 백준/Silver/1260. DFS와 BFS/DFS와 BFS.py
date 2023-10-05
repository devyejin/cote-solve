import sys

input = sys.stdin.readline

# N 정점(노드), M 간선(edge) V (시작 노드 번호, 1부터 시작)
N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)

#DFS, 연결된 노드 중 작은 값 부터 돈다( = 리스트에서 큰 값부터 스택에 넣는다))
stack = []
visited = []

stack.append(V)


while stack:

    cur = stack.pop()
    if cur not in visited:
        visited.append(cur)

        sorted_list = sorted(adj_list[cur],reverse=True)
        for num in (sorted_list):
             stack.append(num) #스택에 값 넣기


print(*visited)

#BFS
from collections import deque
queue = deque()
visited = []

queue.append(V)

while queue:

    cur = queue.popleft()
    if cur not in visited:
        visited.append(cur)

        sorted_list = sorted(adj_list[cur])
        for num in sorted_list:
            queue.append(num)

print(*visited)
