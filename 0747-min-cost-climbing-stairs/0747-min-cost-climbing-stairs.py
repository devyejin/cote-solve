class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1 for _ in range(n+1)]

        def minCost(n:int) -> int:
            if n < 2:
                return 0
            if dp[n] != -1:
                return dp[n]
            dp[n] = min(minCost(n-1)+cost[n-1], minCost(n-2)+cost[n-2])
            return dp[n]

        return minCost(n)


