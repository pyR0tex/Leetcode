# move all 0's to the end of array while maintating relative order of non-zero elements

nums = [1,2,0,0,3,4,0,0,2,0,0]
nums1 = [1,2,0,0,3,4,0,0,2,0,0]

# approach 1: works but ass
def moveZeroes(nums : list[int]) -> None:
    print('approach1:')
    zCount = 0
    for num in nums:
        if num == 0:
            zCount += 1
    for i in range(zCount):
        nums.remove(0)
        nums.append(0)
    print(nums)

# approach2: 2 pointers--hopefully
# j moves inward from right
# i moves inward from left
# loop ends when i and j meet
def moveZeroes1(nums : list[int]) -> None:
    i,j = 0, len(nums) - 1
    while(i < j):
        if(nums[j] == 0):
            j -= 1
        elif(nums[i] == 0):
            nums.insert(j, nums.pop(i))
        else:
            i += 1
    print(nums1)


def main():
    moveZeroes(nums)
    moveZeroes1(nums1)

if __name__ == '__main__':
    main()
