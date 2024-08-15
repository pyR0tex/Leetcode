# given a 1-indexed integer array and a target, return an int array with
# the indeces of integers that add up to the target

numbers, target = [2,2,7,11,15], 9 # return[1,2]
numbers1, target1 = [2,3,4], 6
numbers2, target2 = [-1,0], -1

# works locally, but time limit exceeding on leetcode
def twoSum(numbers : list[int], target : int) -> list[int]:
    i,j,k = 0, len(numbers) - 1, 0;
    for i in range(j):
        k = j
        while(k > i):
            if(numbers[i] + numbers[k] == target):
                return[i+1,k+1]
            k -= 1
        i += 1

def twoSum1(numbers : list[int], target : int) -> list[int]:
    print('approach2')
    i,j = 0, len(numbers) - 1
    while(i < j):
        if((numbers[i] + numbers[j]) == target):
            return [i+1,j+1]
        if((numbers[i] + numbers[j]) < target):
            i += 1
        else:
            j -= 1
    

def main():
    # approach1
    result = twoSum(numbers, target)
    print(result)

    result1 = twoSum(numbers1, target1)
    print(result1)

    result2 = twoSum(numbers2, target2)
    print(result2)
    # end approach1

    # approach2
    result4 = twoSum1(numbers, target)
    print(result4)

if __name__ == '__main__':
    main()
