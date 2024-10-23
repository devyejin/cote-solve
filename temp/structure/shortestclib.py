#완탐 풀이
def shortest(cost) -> int:
    n = len(cost)
    
    dp = {}
        
    #dfs(n) : n층까지 올라오는데 비는 최소의 비용
    def dfs(n) -> int:
        #base condition
        if n == 0 or n ==1:
            dp[n] = 0
            return dp[n]
        
        if n not in dp:
            dp[n] = min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
            return dp[n]
        
        #있는 경우는 그냥 리턴
        return dp[n]    
    
    return dfs(n)

print(shortest([10,15,20])) # 15
print(shortest([1,100,1,1,1,100,1,1,100,1])) #6