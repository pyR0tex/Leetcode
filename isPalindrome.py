# given a string consisting of all characters
# return if its a plindrome after removing non-alphanumeric and upper case characters

s = "A man, a plan, a canal: Panama" # return True
s1 = "race a car" # false
s2 = " " # return true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # approach 1
        print("isPalindrome")
        ss = ''.join(ch for ch in s if ch.isalnum()).lower()
        return ss == ss[::-1]

def main():
    S = Solution()
    flag = S.isPalindrome(s1); print(flag)

if __name__ == '__main__':
    main()
