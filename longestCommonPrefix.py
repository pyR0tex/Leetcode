# given an array of strings, return the longest common prefix among them, else " "

from collections import Counter

strs = ["flower","flow","flight"] # return "fl"
strs1 = ["dog","racecar", "car"] # return ""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        print('longestCommonPrefix')
        # approach:
        # use zip(*strs) to get columns of strs
        # use set to check if all letters are the same
        # add letter to string ans if same
        print(l)
        ans = ""
        for ch in zip(*strs):
            if len(set(ch)) != 1:
                return ans
            else:
                ans += ch[0]
        return ans

def main():
    S = Solution()
    lcp = S.longestCommonPrefix(strs); print(lcp)

if __name__ == '__main__':
    main()
