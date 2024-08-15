# given 2 strings s1 s2, return true if s2 contains a permuation of s1 else false
from collections import Counter
s1 = "ab"
s2 = "eidbaooo" # return True for "ba" -> permuation of "ab"

class Solution:
    # approach1
    # good but not great; runtime is way more than approach 2
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1) # initialize a counter perm string
        l1, l2 = len(s1), len(s2)
        for i in range(l2 - l1 + 1):
            c2 = Counter(s2[i:i+l1])
            if(c1 == c2):
                return True
        return False
    # approach2
    # much better runtime
    # difference is instead of creating a new counter in the loop,
    # create the counter and update it along the way of the loop
    # SLIDING WINDOW
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1) # initialize a counter for s1
        l1 = len(s1) # length of input string
        c2 = Counter(s2[:l1]) # sliding window

        # check if both counters are equal
        if(c2 == c1):
            return True

        # start loop and slide window accordingly
        for i in range(len(s2) - l1):
            # update window dictionary
            if c2[s2[i]] == 1:
                del c2[s2[i]]
            elif c2[s2[i]] > 1:
                c2[s2[i]] -= 1

            if s2[i + l1] in c2:
                c2[s2[i+l1]] += 1
            else:
                c2[s2[i+l1]] = 1

            if c2 == c1:
                return True
        return False

def main():
    S = Solution()
    print(S.checkInclusion(s1, s2))
    print(S.checkInclusion1(s1, s2))

if __name__ == '__main__':
    main()
