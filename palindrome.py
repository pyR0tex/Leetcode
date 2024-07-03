# returns bool if the number is a palxdrome
x0 = 12321 # true
x1 = -121 # false because of -
x2 = 10020012 # false

def isPalindrome(x : int) -> bool:
    # check if negative
    if(x < 0):
        return False

    digits = [int(d) for d in str(x)]
    # check if even or odd
    flag = True if (len(digits)%2) == 0 else False
    i, j = 0, len(digits) - 1
    # for even
    if(flag):
        k = len(digits) // 2
        while(k > 0):
            if(digits[i] == digits[j]):
                i += 1
                j -= 1
            else:
                return False
            k -= 1
        return True
    else:
        k = (i + j) // 2
        while(i < k and j > k):
            if(digits[i] == digits[j]):
                i += 1
                j -= 1
            else:
                return False
        return True

# approach 2
def isPalindrome1(x : int) -> bool:
    dString = str(x)
    return dString == dString[::-1]

def main():
    result0 = isPalindrome(x0)
    result1 = isPalindrome(x1)
    result2 = isPalindrome(x2)
    print(result0)
    print(result1)
    print(result2)

    print("approach2:")
    result4 = isPalindrome1(x0)
    result5 = isPalindrome1(x1)
    result6 = isPalindrome1(x2)
    print(result4)
    print(result5)
    print(result6)


if __name__ == '__main__':
    main()
