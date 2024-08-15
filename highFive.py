# given a list items in which items[i] = [id, score]
# return the max average of top 5 scores for each id
# constraints:
# (1) : items[i].length == 2
# (2): for each id there will be atleast 5 scores

items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# returns [[1,87],[2,88]]

items1 = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
# returns [[1,100],[7,100]]

import heapq
from collections import defaultdict
class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        scores = defaultdict(list)
        for item in items:
            heapq.heappush(scores[item[0]], item[1])
        results = []
        for key,value in scores.items():
            avg = sum(heapq.nlargest(5,value)) // 5
            heapq.heappush(results,[key,avg])

        return results

def main():
    S = Solution()
    highFive = S.highFive(items); print(highFive)

if __name__ == '__main__':
    main()
