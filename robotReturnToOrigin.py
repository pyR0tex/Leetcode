# given a string 'moves' which contains 'L,R,U,D'
# return true if the robot returns to its origin after completing all the moves

moves = "UD" # return true
moves1 = "LL" # return false
moves2 = "UULRDRLD" # return true
from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # approach 1: way slower than counter approach
        # dp = {"L":[-1,0],"R":[1,0],"U":[0,1],"D":[0,-1]}
        # pos = [0,0]
        # for c in moves:
        #     pos[0] += dp[c][0]
        #     pos[1] += dp[c][1]
        # if pos == [0,0]:
        #     return True
        # else:
        #     return False

        # approach 2
        # counter = Counter(moves)
        # if counter["L"] == counter["R"] and counter["U"] == counter["D"]:
        #     return True
        # else:
        #     return False

        # approach 3 : faster than approach 2 with less memory
        # .count() doesnt require the import of Counter
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")

def main():
    S = Solution()
    flag = S.judgeCircle(moves2); print(flag)

if __name__ == '__main__':
    main()
