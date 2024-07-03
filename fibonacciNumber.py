# given an integer n, claculate F(n) -> fibonnaci sequence
n = 2 # return 1
n1 = 3 # return 2
n2 = 4 # return 3

class Solution:
    # approach 1 : mine
    # good approach but runtime is very bad, still intuitive tho
    def fib(self, n: int) -> int:
        print('approach 1: mine but bad runtime')
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        return (self.fib(n - 2) + self.fib(n - 1)) if n > 1 else n
    # approach 2: much faster runtime with same memory usage
    # use equation: F(n) = F(n-2) + F(n-1) given: F(0) = 0, F(1) = 1
    def fib1(self, n: int) -> int:
        print('approach 2: much faster with same memory')
        dp = {0:0,1:1}
        for i in range(2,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

def main():
    S = Solution()
    f = S.fib1(n); print('fn:', f)
    f = S.fib1(n1); print('fn1:', f)
    f = S.fib1(n2); print('fn2:', f)

if __name__ == '__main__':
    main()
