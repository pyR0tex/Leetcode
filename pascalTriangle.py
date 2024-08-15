# given an integer numRows, generate a pascal triangle
# return list[list[int]]

import math

numRows = 5 # return [[1],[1,1],[1,2,1],[1,3,3,1],[1,3,6,4,1]]
numRows1 = 1 # return [[1]]

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # approach
        # initialize a empty triangle with correct dimensions
        result = [[0]*(i+1) for i in range(numRows)]
        # loop for each row
        for line in range(0, numRows):
            # loop for each number in row
            for i in range(0, line + 1):
                # if start or end => 1
                if i == 0 or i == line:
                    result[line][i] = 1
                # ith number is previous line's i-1 + i
                else:
                    result[line][i] = result[line-1][i-1] + result[line-1][i]
        return result



def main():
    S = Solution()
    t = S.generate(numRows);
    for i in t:
        print(i)
    # print(t)

if __name__ == '__main__':
    main()
