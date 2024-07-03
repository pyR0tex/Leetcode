# given an integer numCourses and list[list[int]] prerequisites
# return the ordering of courses you should take to finish all courses
# if there are many valid answers, return any of them
# if its impossible to finish all courses, return an empty array

from collections import deque, defaultdict

numCourses, prerequisites = 2, [[1,0]] # return [0,1]
numCourses1, prerequisites1 = 4, [[1,0],[2,0],[3,1],[3,2]]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        q = deque([])

        for c, p in prerequisites:
            adj[p].append(c)
            indegree[c] += 1

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        print("adj:",adj.items())
        print("indegree:",indegree)
        print("queue:", q)

        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            for c in adj[cur]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        print("adj:",adj.items())
        print("indegree:",indegree)
        print("queue:", q)
        print("ans:", ans)

        return ans if len(ans) == numCourses else []


def main():
    S = Solution()
    result = S.findOrder(numCourses1, prerequisites1)
    print(result)

if __name__ == '__main__':
    main()
