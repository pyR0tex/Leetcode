
# 202. Happy Number

'''
A happy number is a number defined by the following process:

-- Starting with any positive integer,
    replace the number by the sum of the squares of its digits.
-- Repeat the process until the number equals 1 (where it will stay), 
    or it loops endlessly in a cycle which does not include 1.
-- Those numbers for which this process ends in 1 are happy.
'''
from functools import lru_cache
@lru_cache()
def isHappy(n: int) -> bool:
    sums = {}
    def _isHappy(n, sums):
        if n == 1 or n == 7:
            return True
        if n not in sums:
            str_n = str(n)
            sums[str_n] = n
            n = 0
            for s in str_n:
                n += (int(s) ** 2)
            for duplicate in str(n):
                if duplicate in sums:
                    return False
            return _isHappy(n, sums)
        return False
        
    happy = _isHappy(n, sums)
    print(sums)
    return happy
    



def main():
    n = 19
    happy = isHappy(n) # should return TRUE
    print(f"{happy}")

    n = 2
    happy = isHappy(n) # should return FALSE
    print(f"{happy}")

if __name__ == '__main__':

    main()