class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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