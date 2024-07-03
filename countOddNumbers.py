# given 2 numbers low and high, return count of odd numbers inlusive of low and high

low,high = 3,7 # return 3
low1,high1 = 8,10 # return 1
low2 = 800445804
high2 = 979430543
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        print("count odds")
        if high == low:
            return 1 if low%2 != 0 else 0
        numRange = high - low + 1
        if low%2 == 0 or high%2 == 0:
            return numRange // 2
        else:
            return numRange // 2 + 1


def main():
    S = Solution()
    result = S.countOdds(low2,high2); print(result)

if __name__ == '__main__':
    main()
