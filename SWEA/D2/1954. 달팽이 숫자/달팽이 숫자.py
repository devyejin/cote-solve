

          #우0하1좌2상3
dr = (0,1,0,-1)
dc = (1,0,-1,0)


for tc in range(1, int(input())+1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]
    
    r,c,d = 0,0,0

    for num in range(1, N**2 + 1):
        snail[r][c] = num

        nr, nc = r + dr[d], c + dc[d]

        if nc >= N or nc < 0 or nr >= N or nr < 0 or snail[nr][nc] != 0:
            d = ( d + 1 ) % 4
            nr, nc = r + dr[d], c + dc[d]

        r, c = nr, nc

    print(f'#{tc}')
    for row in snail:
        print(*row)
    


  #  우0 하1 좌2 상3
  
dr = ( 0, 1, 0, -1) 
dc = ( 1, 0, -1, 0)

for tc in range(1, int(input() + 1)): #테스트케이스 건 수
    N = int(input())
    
    snail = [[0] * N for _ in range(N)]
    r, c, d = 0, 0, 0
    
    for num in range(1, N ** 2 + 1): #달팽이 크기만큼 순회
        snail[r][c] = num
        
        nr, nc = r + dr[d] , c +dc[d] # 처음엔 우(0)-> 방향
        
        #좌표가 범위 벗어나거나 이미 값 있는 경우 방향 전환
        if nr < 0 or nr >= N or nc nc < 0 or nc >= N or snail[nr][nc] != 0:
            #방향 전환 0~3
            d = (d+1) % 4
            nr, nc = r + dr[d], c + dc[d]
        
        r, c = nr, nc
    
    print(f"#{tc}")
    for ans in snail:
        print(*ans)