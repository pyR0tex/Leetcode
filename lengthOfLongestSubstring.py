# given string s, find the length of the longest substring without repeating characters

s = "abcabcbb" # return 3 for "abc"
s1 = "bbbbb" # return 1 for "b"
s2 = "pwwkew" # return 3 for "wke"
s3 = ""
s4 = " "
s5 = "au"
s6 = "dvdf"
s7 = "anviaj"

# works great
# using dictionary runs faster but more memory
# using the maxLen approach runs slightly slower and alot less memory
def lengthOfLongestSubstring(s: str) -> int:
    # if(len(s) == 0):
    #     return 0
    # elif(len(s) == 1):
    #     return 1
    # sDict = {}
    sList = []
    maxLen = 0
    # splitList = []; splitList[:] = s
    for i in range(len(s)):
        if s[i] in sList:
            # sDict[''.join(sList)] = len(sList)
            sList = sList[sList.index(s[i])+1 :]
        sList.append(s[i])
        if(maxLen < len(sList)):
            maxLen = len(sList)
    # if(sList):
    #     sDict[''.join(sList)] = len(sList)
    #     sList.clear()
    return(maxLen)
    # return max(sDict.values())


def main():
    l = lengthOfLongestSubstring(s)
    l1 = lengthOfLongestSubstring(s1)
    l2 = lengthOfLongestSubstring(s2)
    l3 = lengthOfLongestSubstring(s3)
    l4 = lengthOfLongestSubstring(s4)
    l5 = lengthOfLongestSubstring(s5)
    l6 = lengthOfLongestSubstring(s6)
    l7 = lengthOfLongestSubstring(s7)
    print(l);print(l1);print(l2);print(l3);print(l4);print(l5);print(l6);print(l7)

if __name__ == '__main__':
    main()
