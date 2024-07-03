# you are climbing a staircase that takes int n steps to reach the top
# you can climb either 1 or 2 stairs at once.
# return how many distinct ways there are to climb the stairs

steps = 2 # return 2 (1 step + 1 step and 2 steps)
steps2 = 3 # return 3 (1step+1step+1step, 1step+2steps, 2steps+1step)

class Solution:
    def __init__(self):
        self.memo = {1:1,2:2}

    def climbStairs(self, n: int) -> int:
    # approach 1: bottom up
        if n <= 2: # if n is 1 or 2 => return n
            return n
    # a = 1 step, b = 2 steps
        a,b = 1,2
        for i in range(3,n):
            a, b = b, a+b
        return a+b

    # approach 2: recursion + memoization
    # works much faster due to saving time by memoizing each +1 +2 step into the dictionary
    def climbStairs1(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs1(n-1) + self.climbStairs1(n-2)
        return self.memo[n]

def main():
    S = Solution()
    result = S.climbStairs(10); print(result)
    result = S.climbStairs1(10); print(result)
if __name__ == '__main__':
    main()
