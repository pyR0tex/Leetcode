# find first bad version
n = 90
bad = 18

def isBadVersion(v):
    if(bad <= v):
        return True
    else:
        return False

def findBadVersion(n):
    left, right = 1, n
    while(left < right):
        mid = (left + right) // 2
        if(isBadVersion(mid)):
            right = mid
        else:
            left = mid + 1
    return left

def main():
    result = findBadVersion(n)
    print(result)

if __name__ == '__main__':
    main()
