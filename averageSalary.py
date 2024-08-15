# given an array of unique ints salary where salary[i] is salary of ith employee
# return the average salary of everyone excluding minimum and maximum

salary = [4000,3000,1000,2000] # return 2500.0000
salary1 = [1000,2000,3000] # return 2000
class Solution:
    def average(self, salary: list[int]) -> float:
        print("average salary")
        # approach 1
        # low,high,sum = float('inf'),float('-inf'),0
        # n = len(salary)
        # for i in range(n):
        #     sum += salary[i]
        #     low = min(low, salary[i])
        #     high = max(high, salary[i])
        # sum = sum - high - low
        # return sum/(n-2)

        # approach 2
        # salary.sort()
        # n = len(salary) - 1
        # sum = 0
        # for i in range(1,n):
        #     sum += salary[i]
        # return sum/(n-1)

        # approach 3
        salary.sort()
        summ = sum(salary[1:-1])
        return (summ)/(len(salary)-2)

        # approach 4
        # n = len(salary)
        # low = min(salary)
        # high = max(salary)
        # summ = sum(salary)
        # return(summ-high-low)/(n-2)


def main():
    S = Solution()
    avg = S.average(salary); print(avg)

if __name__ == '__main__':
    main()
