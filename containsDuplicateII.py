# 219. Contains Duplicate II
'''
Given an integer array nums and an integer k, 
return true if there are two distinct indices
i and j in the array such that:
   nums[i] == nums[j]  and
   abs(i - j) <= k.
'''

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    hash = dict()
    for i, num in enumerate(nums):
        if num not in hash:
            hash[num] = i
            continue
        target = abs(i - hash[num])
        if target <= k:
            return True
        else:
            hash[num] = i
    return False



def main():
    nums = [1,2,3,1]
    k = 3
    duplicate = containsNearbyDuplicate(nums, k) # should output TRUE
    print(f"\tk={k}\t{duplicate}\tnums: {nums}")

    nums = [1,0,1,1]
    k = 1
    duplicate = containsNearbyDuplicate(nums, k) # should output TRUE
    print(f"\tk={k}\t{duplicate}\tnums: {nums}")

    nums = [1,2,3,1,2,3]
    k = 2
    duplicate = containsNearbyDuplicate(nums, k) # should output FALSE
    print(f"\tk={k}\t{duplicate}\tnums: {nums}")

    nums = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
    k = 1
    duplicate = containsNearbyDuplicate(nums, k) # should output TRUE
    print(f"\tk={k}\t{duplicate}\tnums: {nums}")
    

if __name__ == '__main__':
    main()
