class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n+1) #memo[i] : i번째 top에 도달하기 위해 지불해야 하는 최소비용
        memo[0] = 0
        memo[1] = 0
        
        def minCost(n:int) -> int: # n번째 top에 도달하기 위해 지불해야 하는 최소비용

            if memo[n] == -1:
                memo[n] = min(minCost(n-1) + cost[n-1], minCost(n-2) + cost[n-2])

            return memo[n]

        return minCost(n)

