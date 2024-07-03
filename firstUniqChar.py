# given a string s, find teh first non-repeating char in it and return its index, else -1

from collections import Counter

s = "leetcode" # return 0
s1 = "loveleetcode" # return 2

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # approach 1
        # use counter to counter letters in s
        # return the index of the first 1
        # else return -1(contains no singles)
        c = Counter(s)
        for i in c:
            if c[i] == 1:
                return s.index(i)
        return -1

def main():
    S = Solution()
    flag = S.firstUniqChar(s); print(flag)
    flag = S.firstUniqChar(s1); print(flag)

if __name__ == '__main__':
    main()
