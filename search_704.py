# search an ascending number list for target
# return index of target in list

nums = [1,2,3,4,5,6,7,8,9,15,35,55,66,67,69,420]
target = 6 #return value 5
# approach 1 => binary search
def search1(nums, target: int) -> int:
    left, right = 0, len(nums) - 1
    while(left <= right):
        mid = (left + right) // 2
        if(target == nums[mid]):
            return mid
        elif(target < nums[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return -1
# approach 2 => not binary search
def search2(nums, target: int) -> int:
    return nums.index(target) if target in nums else -1

def main():
    result1 = search1(nums, target)
    result2 = search2(nums, target)
    print(result1)
    print(result2)

if __name__ == '__main__':
    main()
