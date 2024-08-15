#search where to insert a target int in a sorted array
#if target already there, return index

nums1 = [1,4,6,8,10,14,25]
nums2 = [1,4,6,8,10,14,25]
nums3 = [1,3,5,6]
nums4 = [-10,-6,-1,0,1,2,5,7,8]

target1 = 8 # return value: 3
target2 = 5 # return value : 2
target3 = 2 # return value : 1
target4 = -11 # return value: 0

def searchInsert(nums, target: int) -> int:
    left, right = 0, len(nums) - 1
    while(left <= right):
        mid = (left + right) // 2
        if(target == nums[mid]):
            return mid
        elif(target < nums[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return left
def main():
    result = searchInsert(nums4, target4)
    print(result)

if __name__ == '__main__':
    main()
