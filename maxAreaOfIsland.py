# given a MxN grid, return the max are of an island
# island is a 4-directional related sqaures that contain 1

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]] # result = 6
for i in grid: print(i)


# approach:
# only call dfs on islands
# keep track of area with max function everytime it encounters a 1

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        maxLen = 0
        # DFS function
        # check r,c are out of grid bounds
        # check if grid[r][c] is not 1
        # return a sum of all areas that are connected 4 directionally
        def dfs(r,c):
            if r<0 or c<0 or r>rows-1 or c>cols-1 or grid[r][c] != 1:
                return 0

            grid[r][c] = -1
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        # loop over each grid index
        # call dfs on any 1 encountered
        # dfs function will recursively call itself until all connecting 1's are exhausted
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxLen = max(maxLen, dfs(r,c))

        return maxLen

def main():
    S = Solution()
    area = S.maxAreaOfIsland(grid); print(area)

if __name__ == "__main__":
    main()
