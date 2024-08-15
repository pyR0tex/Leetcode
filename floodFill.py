# perform a flood fill on image(mxn grid) starting from pixel image[sr][sc] with newColor
# flood fill: from starting pixel, and 4-directinal pixels from image[sr][sc]; replace
#             all pixels with newColor

image = ([[1,1,1],
          [1,1,0],
          [1,0,1]]); print("\nimage:");
for i in range(len(image)): print(image[i])

image1 = ([[1,1,1],
           [1,1,0]]); print("\nimage1:");
for i in range(len(image1)): print(image1[i])

sr, sc, newColor = 1, 1, 2; print("\nsr:",sr); print("sc:", sc); print("newColor:", newColor,'\n')

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        length = len(image) # rows
        width = len(image[0]) # cols
        color = image[sr][sc] # color of starting point

        def DFS(l,w):
            # check criteria for dfs
            # (1) indeces beyond grid dimensions
            # (2) new cell is different color than src color
            # (3) new cell is same color as new color => visited
            if l<0 or w<0 or l>length-1 or w>width-1 or image[l][w] == newColor or image[l][w] != color: #(1)
                return
            # change color
            image[l][w] = newColor
            # recur on all 4 dimensions
            DFS(l+1,w)
            DFS(l-1,w)
            DFS(l,w+1)
            DFS(l,w-1)
        # call dfs for the first time
        DFS(sr,sc)
        return image

def main():
    S = Solution()
    f1 = S.floodFill(image, sr, sr, newColor)
    f2 = S.floodFill(image1, sr, sr, newColor)


if __name__ == '__main__':
    main()
