#input이 인접행렬

from collections import deque

#상우하좌
dn=[-1,0,1,0]
dm=[0,1,0,-1]

def solution(maps):
    n = len(maps)
    m = len(maps[0]) 
    
    def bfs(start_n,start_m):
        Q = deque()
        Q.append((start_n,start_m))
        maps[start_n][start_m] = 0 #방문 표시
        
        dist = [[-1] * m for _ in range(n)] #거리 저장
        dist[start_n][start_m] = 1 #시작 지점 거리
        
        while Q:
            curr_n, curr_m = Q.popleft()
            
            #4방향
            for i in range(4):
                nn = curr_n + dn[i]
                nm = curr_m + dm[i]

                if 0 <= nn < n and  0 <= nm < m and maps[nn][nm] == 1: #갈 수 있다면
                    Q.append((nn, nm))
                    maps[nn][nm] = 0
                    dist[nn][nm] = dist[curr_n][curr_m] + 1 #거리 업데이트
                
                #도착지인지 체크
                if nn == n -1 and nm == m-1:
                    return dist[nn][nm]
                
        return -1 #도착 못 하는 경우
    
    result = bfs(start_n = 0, start_m = 0)
    
    return result