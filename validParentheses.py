# given a string containing '(,),{,},[,]' return True if it contains valid parentheses
# constraints:
# (1) open brackets must be closed by the same type of brackets
# (2) open brackets must be closed in the correct order

s = "()" # true
s1 = "()[]{}" # true
s2 = "(]" # false
s3 = "["

class Solution:
    def isValid(self, s: str) -> bool:
        print('isValidParentheses')
        # approach:
        # make a dictionary mapping of brackets
        # loop through string and push open brackets onto stack
        # if closed bracket encountered: check constraints
        # (1): if stack is empty return false
        # (2): if brackets dont match return False
        # at the end: if all brackets matched and stack is not empty return False else True
        d = {'(':')',
             '[':']',
             '{':'}'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if d[opening] != i:
                    return False
        return False if stack else True

def main():
    S = Solution()
    flag = S.isValid(s1); print(flag)

if __name__ == '__main__':
    main()
