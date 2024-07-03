# given an int x, return its integer square root. Cant use builtin functions(** or pow)

x = 4 # return 2
x1 = 8 # return 2 becasue sqrt(8) = 2.8...
x2 = 15 # return 3
x3 = 50

class Solution:
    def mySqrt(self, x: int) -> int:
    # horrible run time on solution
    # brute force approach:
        # for i in range(x + 1):
        #     if i*i == x:
        #         return i
        #     elif i*i > x:
        #         return i-1

    # approach 2: binary search
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if (mid * mid) <= x < ((mid+1)*(mid+1)):
                return mid
            elif x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1


def main():
    S = Solution()
    result = S.mySqrt(x3); print(result)

if __name__ == '__main__':
    main()
