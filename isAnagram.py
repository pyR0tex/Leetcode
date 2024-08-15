# given 2 strings s and t, return True if t is an anagram of s, else false

from collections import Counter

s,t = "anagram","nagaram"
s1,t1 = "rat","car"
class Solution():
    def isAnagram(self, s: str, t: str) -> bool:
        # approach:
        # very easy; if both counters do not equal, return False else true
        # if Counter(s) != Counter(t):
        #     return False
        # return True

        # approach 2
        # almost same as approach 1
        return Counter(s) == Counter(t)

def main():
    S = Solution()
    flag = S.isAnagram(s,t); print(flag)
    flag = S.isAnagram(s1,t1); print(flag)

if __name__ == '__main__':
    main()
