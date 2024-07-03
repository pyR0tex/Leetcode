# given 2 string ransomNote and magazine, return true if ransomNote can be
# constructed from magaizine, else false
#(1) each letter in magazine can only be used once in ransome note

from collections import Counter

ransomNote, magazine = "a", "b" # return False
ransomNote1, magazine1 = "aa", "ab" # return False
ransomNote2, magazine2 = "aa", "aab" # return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str)->bool:
        # approach
        # use counter to count each letter in ransomNote and magazine
        # if key in ransom doesnt exits in magazine => return False
        # if key.count in ransom greater than key.count magazine => return False
        # once everything checks out, return true
        r = Counter(ransomNote)
        m = Counter(magazine)
        for count in r:
            if count not in m or r[count] > m[count]:
                return False
        return True


        # # approach 2
        # # use set of ransomNote to check if its greater than magazine
        
        # for i in set(ransomNote):
        #     if ransomNote.count(i) > magazine.set(i):
        #         return False
        # return True


def main():
    S = Solution()
    flag = S.canConstruct(ransomNote, magazine); print(flag)
    flag = S.canConstruct(ransomNote1, magazine1); print(flag)
    flag = S.canConstruct(ransomNote2, magazine2); print(flag)

if __name__ == "__main__":
    main()
