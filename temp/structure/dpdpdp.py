#dp bottom-up 방식
def shortest(cost) -> int:
    n = len(cost)
    dp = {}
    
    #dfs(n) : n층까지 올라오는데 드는 최소 비용
    def dfs(n) -> int:
        #base condition 
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]
    
    return dfs(n)

print(shortest([10,15,20])) # 15
print(shortest([1,100,1,1,1,100,1,1,100,1])) #6