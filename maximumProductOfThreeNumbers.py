# given an array nums, return the maximum product of 3 numbers

nums = [1,2,3] # return 6
nums1 = [1,2,3,4] # return 24
nums2 = [-1,-2,-3] # return -6
nums3 = [-100,-98,-1,2,3,4] # return 24

import heapq
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        print("maximumProduct")
        # approach 1: had the right idea the whole time but missed the max part in line 17
        # faster approach. GOOD JOB
        prod = 1
        large = heapq.nlargest(3,nums)
        small = heapq.nsmallest(2,nums)
        prod = max(small[0]*small[1]*large[0],large[0]*large[1]*large[2])
        return prod

        # approach 2: didnt need heap
        # nums.sort()
        # return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])

def main():
    S = Solution()
    maxProd = S.maximumProduct(nums3); print(maxProd)

if __name__ == '__main__':
    main()
