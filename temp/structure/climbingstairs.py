#완탐

cost = [10, 15, 20, 17, 1]
def dfs(n):
    
    #min((n-1)층에서 올라가기 (n-2)층에서 올라가기)
    if n == 0 and n == 1:
        return 0
    return min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2]) # O(2^n) -> 높은 시간 복잡도, n = 1000이니 시간초과남

#반복되니 memoization이용
memo = {}
cost = [10, 15, 20, 17, 1]

def dp(n):
    
    if n == 0 and n == 1:
        return 0
    
    if n not in memo:
        memo[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2]) #O(2n) = O(n) : 한 번만 훑어보면 됨
    return memo[n]

print(dp(5))

#top down 방식
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {} #n층까지 가는 최소 비용
        n = len(cost)
        
        if n == 0 or n == 1:
            return 0
        
        if n not in memo:
            memo[n] = min (memo[n-1] + cost[n-1], memo[n-2] + cost[n-2])
        
        return memo[n]