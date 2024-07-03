# given an int n, return Tn => Tribonacci sequence
# givens: T0 = 0, T1 = 1, T2 = 1, Tn+3 = Tn + Tn+1 + Tn+2 for n > 0
from functools import lru_cache
n = 4 # return 4
n1 = 30 # return 1389537

class Solution:
    # approach 1: mine, idea from fibonacci MEMOIZATION
    # use a dictionary for given values
    # iterate from 3 all the way to n+1 and return dic[n]
    def tribonacci(self, n: int) -> int:
        dic = {0:0,1:1,2:1}
        for i in range(3,n+1):
            dic[i] = dic[i-3] + dic[i-2] + dic[i-1]
        return dic[n]

    # approach 2: recursive
    # much much slower without lru_cache -- time limit exceed on leetcode
    # its actually pretty fast with lru_cache.
    @lru_cache(None)
    def tribonacci1(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        return (self.tribonacci1(n - 3) + self.tribonacci1(n - 2) + self.tribonacci1(n - 1))

def main():
    S = Solution()

    print('approach 1: iterative with dictionary')
    trib = S.tribonacci(n); print('tn:',trib)
    trib = S.tribonacci(n1); print('tn1',trib)
    print('')
    print('approach 2: recursive')
    trib = S.tribonacci1(n); print('tn:',trib)
    trib = S.tribonacci1(n1); print('tn1',trib)

if __name__ == '__main__':
    main()
