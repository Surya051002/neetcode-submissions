class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {}

        def check(i):
            # Base case: if we've reached or passed the top, cost is 0
            if i >= n:
                return 0
            
            # Return cached result if we already solved this
            if i in dp:
                return dp[i]
            
            # Choose the minimum cost between taking 1 step or 2 steps
            dp[i] = cost[i] + min(check(i + 1), check(i + 2))
            return dp[i]

        # You can start from step 0 or step 1
        return min(check(0), check(1))