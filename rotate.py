# rotates array k times to the right
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
nums1 = [1,2,3,4,5,6,7,8,9,10,11,12]
k = 5

def rotate(nums, k : int) -> None:
    k = k % len(nums)
    if(k == 0):
        return
    nums[:] = nums[-k:] + nums[:-k]

def rotate1(nums, k : int) -> None:
    k = len(nums) - (k % len(nums))
    while(k > 0):
        nums.append(nums.pop(0))
        k -= 1

def main():
    rotate(nums, k)
    print(nums)

    rotate1(nums1, k)
    print(nums1)

if __name__ == '__main__':
    main()
