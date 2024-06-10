class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n+1) #memo[i] : i번째 top에 도달하기 위해 지불해야 하는 최소비용
        memo[0] = 0
        memo[1] = 0

        #bottom up으로 밑에서부터 채워간다면
        
        for i in range(2, n+1):
            memo[i] = min(memo[i-1] + cost[i-1]  , memo[i-2] + cost[i-2] )

        return memo[n]

