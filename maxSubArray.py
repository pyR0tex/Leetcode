# given array nums, find the contiguous subarray(containing atleast 1 number)
# which has the largest sum and return its sum
nums = [-2,1,-3,4,-1,2,1,-5,4] # 6 for [4,-1,2,1]
# nums1 = [1] # 1 for [1]
# nums2 = [5,4,-1,7,8] # 23 for all of array
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # approach: use Kadane's algorithm
        # It describes this exact problem(longest contiguous subarray sum)
        curSum = sum = nums[0]
        for i in nums[1:]:
            curSum = max(i, curSum + i)
            sum = max(curSum, sum)
        return sum
        print("maxSubArray")



def main():
    S = Solution()
    flag = S.maxSubArray(nums); print(flag)
    # flag = S.maxSubArray(nums1); print(flag)
    # flag = S.maxSubArray(nums2); print(flag)

if __name__ == '__main__':
    main()
