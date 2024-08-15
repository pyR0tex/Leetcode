# given an array of strings, group the anagrams together. return ans in any order

strs = ["eat","tea","tan","ate","nat","bat"]
# return [["bat"],["nat","tan"],["ate","eat","tea"]]

strs1 = [""] # return [[""]]
strs2 = ["a"] # return [["a"]]
strs3 = ["","b",""] # return [["",""],["b"]]

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # approach 1: understand defaultdict more
        # if key error: defaultdict will put in a []
        # sorted() will break string into sorted list
        # you can append because defaultdict(LIST)
        d = defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            d[ss].append(s)
        return d.values()

def main():
    S = Solution()
    anagrams = S.groupAnagrams(strs); print(anagrams)

if __name__ == '__main__':
    main()
