# twoSum.py 

def twoSum(nums: list[int], target: int) -> list[int]:
    print("Two Sum")
    indexMap = {}
    for i in range(0, len(nums)):
        dummy = abs(target - nums[i])
        if dummy not in indexMap:
            indexMap[nums[i]] = i
        else:
            return [indexMap[dummy], i]
    return []


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    TwoSum = twoSum(nums, target) # return[0,1] or [1,0]
    print([ts for ts in TwoSum])

    nums = [3,2,4]
    target = 6
    TwoSum = twoSum(nums, target) # return[1,2] or [2,1]
    print([ts for ts in TwoSum])

    nums = [3,3]
    target = 6
    TwoSum = twoSum(nums, target) # return[0,1]
    print([ts for ts in TwoSum])

    nums = [-3,4,3,90]
    target = 0
    TwoSum = twoSum(nums, target) # return[0,2]
    print([ts for ts in TwoSum])