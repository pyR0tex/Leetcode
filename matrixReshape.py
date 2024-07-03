# given a MxN matrix and ints r,c = num rows num cols, return the reshaped matrix
# if not possible to reshape, return original matrix

mat = [[1,2],
       [3,4]]; r,c = 1,4; print('row:',r,'col:',c)
for i in mat: print(i)


class Solution:
    def reshapeMatrix(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows*cols != r*c:
            return mat
        result = []
        finalResult = [[0]*c for _ in range(r)]
        for row in range(rows):
            for col in range(cols):
                result.append(mat[row][col])
        for row in range(r):
            for col in range(c):
                finalResult[row][col] = result.pop(0)

        return finalResult


def main():
    S = Solution()
    result = S.reshapeMatrix(mat, r, c); print(result)
    # print(result)

if __name__ == '__main__':
    main()
