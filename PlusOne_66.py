# 66. Plus One 

def plusOne(digits: list[int]) -> list[int]:
    print("Plus One start")
    rList = digits[::-1] # reverses the list
    if rList[0] != 9:
        rList[0] += 1
        return rList[::-1]
    counter = 0
    carry = False
    for digit in rList:
        if digit == 9:
            carry = True
            rList[counter] = 0
        else:
            rList[counter] += 1
            return rList[::-1]
        counter += 1
    if carry:
        rList.append(1)
    return rList[::-1]

if __name__ == '__main__':
    in1 = [1,2,3] # out: [1,2,4]
    in2 = [4,3,2,2] # out: [4,3,2,3]
    in3 = [9] # out: [1,0]
    in4 = [6,9,9] # out: [7,0,0]
    in5 = [2] # out: [3]
    in6 = [9,9] # out: [1,0,0]

    # in1
    solution = plusOne(in1)
    strSolution = ','.join(str(s) for s in solution)
    print("in1: " + "[" + strSolution + "]")

    # in2
    solution = plusOne(in2)
    strSolution = ','.join(str(s) for s in solution)
    print("in2: " + "[" + strSolution + "]")

    # in3
    solution = plusOne(in3)
    strSolution = ','.join(str(s) for s in solution)
    print("in3: " + "[" + strSolution + "]")

    # in4
    solution = plusOne(in4)
    strSolution = ','.join(str(s) for s in solution)
    print("in4: " + "[" + strSolution + "]")

    # in5
    solution = plusOne(in5)
    strSolution = ','.join(str(s) for s in solution)
    print("in5: " + "[" + strSolution + "]")

    # in6
    solution = plusOne(in6)
    strSolution = ','.join(str(s) for s in solution)
    print("in6: " + "[" + strSolution + "]")