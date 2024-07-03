# determine if a 9x9 sudoku is valid. Only the filled cells need to be validated
# rules:
# 1.Each row must contain the digits 1-9 without repetition.
# 2.Each column must contain the digits 1-9 without repetition.
# 3.Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
#   without repetition.

from collections import defaultdict

b = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9",".",".",".",".",".","6","."]
    ,["5",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
for i in b: print(i)

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # approach:
        # have 3 dicts holding row, col, and square values
        # check each time if num in any dicts, else add num
        # row, col, sq = defaultdict(set),defaultdict(set),defaultdict(set)
        # for i in range(9):
        #     for j in range(9):
        #         num = board[i][j]
        #         if num.isdigit():
        #             square = (i//3,j//3)
        #             if num in row[i] or num in col[j] or num in sq[square]:
        #                 return False
        #             else:
        #                 row[i].add(num)
        #                 col[j].add(num)
        #                 sq[square].add(num)
        # return True
        n = 9
        rows,cols,boxes = [],[],[]
        for _ in range(n):
            rows.append(set())
            cols.append(set())
            boxes.append(set())
        

def main():
    S = Solution()
    flag = S.isValidSudoku(b);
    print(flag)

if __name__ == '__main__':
    main()
