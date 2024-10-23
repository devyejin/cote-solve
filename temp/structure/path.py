#(0,0) -> (r,c)까지 도착하는 unique path의 수
# (r-1, c)까지 도착하는 unique path의 수 + (r, c-1)까지 도착하는 unique path의 수

def uniquePaths(m,n):
    memo = [[-1] * n for _ in range(m)]

    #초기값
    for r in range(m):
        memo[r][0] = 1
    for c in range(n):
        memo [0][c] = 1

    for r in range(1, m):
        for c in range(1, n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1]
    
    return memo[m-1][n-1]


print(uniquePaths(3,7))