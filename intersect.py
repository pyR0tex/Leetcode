# given 2 integer arrays, return their intersections
n1,n2 = [1,2,2,1], [2,2] # return [2,2]
n3,n4 = [4,9,5], [9,4,9,8,4] # [4,9] or [9,4]

from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # both good approaches and run around the same time
        # I like the second approaches shorter code though

        if(len(nums2) < len(nums1)): return self.intersect(nums2, nums1)
        c1, c2 = Counter(nums1), Counter(nums2)
        rList = []
        for key in c1.keys():
            if key in c2.keys():
                x = min(c1[key], c2[key])
                while x > 0:
                    rList.append(key)
                    x -= 1
        return rList
        # c1 = Counter(nums1)
        # c2 = Counter(nums2)
        # output = []
        # for key in c1.keys() & c2.keys():
        #     output.extend([key]*min(c1[key], c2[key]))
        #
        # return output

def main():
    S = Solution()
    r = S.intersect(n1,n2); print(r)
    r1 = S.intersect(n3,n4); print(r1)

if __name__ == '__main__':
    main()
