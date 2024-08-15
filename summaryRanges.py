# 228. Summary Ranges

'''
Q.  Given a sorted unique array -> nums
    Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

    Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b 
'''


def summaryRanges(nums: list[int]) -> list[str]:
    summaryRanges = []
    curRange = []
    for i, num in enumerate(nums):
        print(f"\ti: {i} \t num: {num}")
        if num-1 in curRange:
            curRange.append(num)
        else:
            if len(curRange) == 0:
                curRange.append(num)
            elif len(curRange) == 1:
                summaryRanges.append(f"{curRange[0]}")
            else:
                summaryRanges.append(f"{curRange[0]}->{curRange[-1]}")
            curRange.clear()
            curRange.append(num)
        # print(f"curRange: {curRange}")
        # print(f"summaryRange: {summaryRanges}")
    if len(curRange) == 1:
        summaryRanges.append(f"{curRange[0]}")
    elif len(curRange) >= 2:
        summaryRanges.append(f"{curRange[0]}->{curRange[-1]}")
    return summaryRanges


def main():
    nums = [0,1,2,4,5,7]
    summaryRange = summaryRanges(nums)
    print([s for s in summaryRange]) # return ["0->2","4->5","7"]

    nums = [0,2,3,4,6,8,9]
    summaryRange = summaryRanges(nums)
    print([s for s in summaryRange]) # return ["0","2->4","6","8->9"]


if __name__ == '__main__':
    main()