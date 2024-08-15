# given 2 sorted arrays in non-descending order, return a merged sorted array

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]   # return [1,2,2,3,5,6]
m, n = 3, 3

nums3 = [1,2,3,0,0,0]
nums4 = [2,5,6]   # return [1,2,2,3,5,6]
m1, n1 = 3, 3

########
# both approaches produce similr results on leetcode
########
class Solution:
    def merge(self, nums1: list[int], nums2: list[int], m: int, n: int) -> None:
        print('merge')
        # approach 1
        # put all of nums2 at all the 0's in nums1 and call sort()
        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()

    def merge1(self, nums1: list[int], nums2: list[int], m: int, n: int) -> None:
        # more intuitive approach
        # work backwards through nums1 and nums2 and put it in nums1[k]
        print('better merge')
        i, j, k = m-1, n-1, m+n-1
        while j >= 0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
def main():
    S = Solution()
    # approach 1
    S.merge(nums1,nums2,m,n); print(nums1)
    # approach 2
    S.merge1(nums3,nums4,m1,n1); print(nums3)

if __name__ == '__main__':
    main()
