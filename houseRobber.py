# given an array nums representing cash stashed in each num[i]
# return the maximum amount of cash you can rob
# constraints: cant rob adjacent houses

nums = [1,2,3,1] # return 4
nums1 = [2,7,9,3,1] # return 12

class Solution:
    def rob(self, nums: list[int]) -> int:
        print('houseRobber')
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = {0:nums[0],1:max(nums[0],nums[1])}
        for i in range(2,n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]

def main():
    S = Solution()
    cash = S.rob(nums); print(cash)

if __name__ == '__main__':
    main()
