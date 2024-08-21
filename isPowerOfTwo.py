# 231. Power of Two
'''
Given an int n, return TRUE if it si a poer of 2; else return FALSE
n is a power of two, if x exists such that n == 2^x
'''


def isPowerOfTwo(n: int) -> bool:
    powerOfTwo, x = 0, 0
    if n <= 0:
        return False
    powerOfTwo = 2 ** x
    while powerOfTwo < n:
        powerOfTwo = 2 ** x 
        x += 1
    if powerOfTwo == n:
        return True
    return False

    '''
    Solutions with some neat math:
    
    code:
    return (n > 0) and (n & (n-1) == 0)

        OR

    If a number is power of 2, there exists 1 and only 1 bit-1
      in the binary of this number, such as 0b10, 0b100, 0b1000.

    code:
    return n > 0 and bin(n).count('1') == 1

    '''

def main():
    n = 8
    flag = isPowerOfTwo(n)
    print(flag)



if __name__ == '__main__':
    main()
