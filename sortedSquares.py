# takes non-decreasing sorted array and return non-decreasing sorted array with each square
nums = [-4,-1,0,3,10] # return value [0,1,9,16,100]
nums1 = [-4,-1,0,3,10] # return value [0,1,9,16,100]
nums2 = [-7,-3,2,3,11] # return value [4,9,9,49,121]
# trivial solution. faster than 13.3% :(
def sortedSquares(nums):
    for num in range(len(nums)):
        nums[num] = nums[num] * nums[num]
    nums.sort()
    return nums

# optimized approach (2 pointers)
def sortedSquares1(nums):
    i,j,k = 0, len(nums) - 1, len(nums) - 1
    result = [0] * len(nums)
    while k >= 0:
        curI = nums[i] ** 2
        curJ = nums[j] ** 2
        if curI > curJ:
            result[k] = curI
            i += 1
        else:
            result[k] = curJ
            j -= 1
        k -= 1
    print(result)
    return result

# fastest approach, more memory => one-liner
def sortedSquares2(nums):
    return sorted([x*x for x in nums])

def main():
    result1 = sortedSquares(nums)
    result2 = sortedSquares(nums)
    print('trivial solution:')
    print(result1)
    print(result2)
    # for optimized solution
    result3 = sortedSquares1(nums1)
    result4 = sortedSquares1(nums2)
    print('optimized solution:')
    print(result3)
    print(result4)
    # for one-liner
    result5 = sortedSquares1(nums1)
    result6 = sortedSquares1(nums2)
    print('one-liner solution')
    print(result5)
    print(result6)


if __name__ == '__main__':
    main()
