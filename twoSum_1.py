# given an array nums and a target, return the indices of the 2 numbers that sum to target

nums, target = [2,7,11,15], 9 #return [0,1]
nums1, target1 = [3,2,4], 6 #return [1,2]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # approach 1:
        # use hash table to store target - nums[i]
        # hashmap used because key=value pairs are much faster to look up than array manipulation
        
        d = {}
        for index, num in enumerate(nums):
            diff = target - nums[index]
            if diff in d:
                return[index, d[diff]]
            d[num] = index



def main():
    S = Solution()
    flag = S.twoSum(nums, target); print(flag)
    flag = S.twoSum(nums1, target1); print(flag)

if __name__ == '__main__':
    main()
