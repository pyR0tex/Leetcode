import random
import string

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        
        index = 0
        for letter in t:
            if letter == s[index]:
                index += 1
            if index >= len(s):
                return True
        return False
    
    def generateRandomString(self, flag: str) -> str:
        if flag == "s":
            length = random.randint(0,5)
        elif flag == "t":
            length = random.randint(0,100)
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def main():
    sol = Solution()
    s = sol.generateRandomString('s')
    t = sol.generateRandomString('t')
    print(f"s:",s)
    print(f"t:",t)

    isSubsequence = sol.isSubsequence(s,t)
    print(isSubsequence)

if __name__ == '__main__':
    main()
    