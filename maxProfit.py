# given an array prices where prices[i] is the price of stock on ith day
# return the max profit you can make when you buy then sell
# return 0 if you cant make profit

p = [7,1,5,3,6,4] # return 5 for 6-1 = 5
p1 = [7,6,5,4,3,1] # return 0 as no profit can be made

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        print('maxProfit')
        # approach
        # very inuitive solution
        # takes care of buy before sell by doing min price and profit calc first
        # then updates maxProfit after
        maxProfit = 0
        minPrice = float('inf')
        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit
        # return 0
def main():
    S = Solution()
    profit = S.maxProfit(p); print(profit)
    profit = S.maxProfit(p1); print(profit)

if __name__ == '__main__':
    main()
