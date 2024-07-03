# given an array nums, return True if any value is duplicate, else false

from collections import Counter

nums = [1,2,3,1] # true
nums1 = [1,2,3,4] # false
nums2 = [1,1,1,3,3,4,3,2,4,2] # true
nums3 = [0]
nums4 = [3,3]

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # approach 1
        # use counter to keep frequencies
        c = Counter(nums)
        for i in c.values():
            if i > 1:
                return True
        return False

    def containsDuplicate1(self, nums: list[int]) -> bool:
        # approach 2
        # use set(), it keeps values without repetition
        # if the set length is not the same as length of nums, return True else false
        return len(set(nums)) != len(nums)

def main():
    S = Solution()
    flag = S.containsDuplicate(nums); print(flag)
    flag = S.containsDuplicate(nums1); print(flag)
    flag = S.containsDuplicate(nums2); print(flag)
    flag = S.containsDuplicate(nums3); print(flag)
    flag = S.containsDuplicate(nums4); print(flag)

    flag = S.containsDuplicate1(nums); print(flag)
    flag = S.containsDuplicate1(nums1); print(flag)
    flag = S.containsDuplicate1(nums2); print(flag)
    flag = S.containsDuplicate1(nums3); print(flag)
    flag = S.containsDuplicate1(nums4); print(flag)
    
if __name__ == '__main__':
    main()
