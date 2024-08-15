# given an int array cost where cost[i] is the cost of the ith step on the staircase
# once you pay, you can climb either 1 or 2 steps
# you can either start from the step with index 0 or index 1
# RETURN THE MINIMUM COST TO REACH THE TOP

cost = [10,15] # return 15
cost1 = [1,100,1,1,1,100,1,1,100,1] # return 6

class Solution:
    # approach 1: using dp for memoization (almost had it right besides the return statement)
    # returns the best value in dp last 2
    # almost same as fibonacci except "cost[i] +" and the return statement
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        print('minCost')
        n = len(cost)
        dp = {0:cost[0],1:cost[1]}
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])

def main():
    S = Solution()
    minCost = S.minCostClimbingStairs(cost1); print(minCost)

if __name__ == '__main__':
    main()
