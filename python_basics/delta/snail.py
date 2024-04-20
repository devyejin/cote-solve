# 우 하 좌 상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

for tc in range(int(input())):
    N = int(input())
    
    snail = [[0] * N for _ in range(N)]
    r, c, d = 0, 0, 0
    
    #달팽이 돌 시간~
    for num in range(1, N **2 + 1):
        
        #갑 할당
        snail[r][c] = num
        
        #다음 좌표 설정
        nr, nc = r + dr[d], r + dc[d]
        
        #nr, nc가 범위 내 인지 + 방문 안한 곳인지 체크 -> 방향 전환
        if nr < 0 or nr >= 3 or nc < 0 or nc >= 3 or snail[nr][nc] != 0:
            d = ( d + 1 ) % 4
            
            nr, nc = r +dr[d], r +dc[d] #방향 전환 후 값
            
        r, c = nr, nc #좌표 설정해주고 끝 (값 할당으로 시작은 위에서)
        
    print(f"#{tc}")
    for ans in snail:
        print(*ans)
        
        
