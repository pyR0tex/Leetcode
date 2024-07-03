# write an efficient algo that searches mxn matrix for a target.
# properties of matrix:
# (1) ints in each row are sorted from left to right
# (2) the first int of each row is greater than last int previous row
import bisect as B
m = [[1,3,5,7],
     [10,11,16,20],
     [23,30,34,60]]
m1 = [[1,3,5,7],
      [10,11,16,20],
      [23,30,34,60]]

target = 3 # output = True
target1 = 13 # output = False

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        print('searchMatrix')
        # approach 1:
        # advanced binary search
        # use internal module bisect, which uses binary search
        # check if target is valid
        if not(matrix[0][0] <= target <= matrix[-1][-1]):
            return False

        row = B.bisect_right(next(zip(*matrix)), target) - 1; print(row)
        col = B.bisect_right(matrix[row], target) - 1; print(col)
        return target == matrix[row][col]

    def searchMatrix1(self, matrix: list[list[int]], target: int) -> bool:
        # approach2
        # makes alot more sense, personally
        # idea: in each row, check if target less than last elem in that row
        # if elem smaller, check that row if target in there
        m = len(matrix)
        for row in range(m):
            last = matrix[row][-1]
            if target <= last:
                if target in matrix[row]:
                    return True
        return False
def main():
    S = Solution()
    flag = S.searchMatrix(m, target); print(flag)
    flag = S.searchMatrix(m1, target1); print(flag)

if __name__ == '__main__':
    main()
