# 67. Add Binary

def addBinary(a: str, b:str) -> str:
    solution = []
    # store input strings as lists
    listA = [charA for charA in a]
    listB = [charB for charB in b]
    print([x for x in listA])
    print([x for x in listB])

    # get length of  binary number
    lenA = len(listA)
    lenB = len(listB)
    print("Length a: " + str(lenA) + " Length b: " + str(lenB))

    # get Max Length of binary numbers
    maxLen = max(lenA, lenB)
    print("Max Length: " + str(maxLen))
    if lenA > lenB:
        index = lenA - lenB
        for i in range(0, index):
            listB.insert(0, "0")
    elif lenB > lenA:
        index = lenB - lenA
        for i in range(0, index):
            listA.insert(0, "0")
    elif lenA == lenB:
        print("Same Size Binary Number")
    print("Lists with leading zeroes:")
    print([x for x in listA])
    print([x for x in listB])
    # reverse lists
    listA = listA[::-1]
    listB = listB[::-1]
    # Logic start
    carry = 0
    for i in range(0, maxLen):
        if listA[i] == "1" and listB[i] == "1":
            if carry == 1:
                solution.append("1")
                carry = 1
            else:
                solution.append("0")
                carry = 1
        elif listA[i] == "0" and listB[i] == "1":
            if carry == 1:
                solution.append("0")
                carry = 1
            else:
                solution.append("1")
                carry = 0
        elif listA[i] == "1" and listB[i] == "0":
            if carry == 1:
                solution.append("0")
                carry = 1
            else:
                solution.append("1")
                carry = 0
        elif listA[i] == "0" and listB[i] == "0":
            if carry == 1:
                solution.append("1")
                carry = 0
            else:
                solution.append("0")
                carry = 0
    if carry == 1:
        solution.append("1")
    solution = solution[::-1]
    print([str(s) for s in solution])

    return ''.join(solution)


# Main
if __name__ ==  '__main__':
    
    # test 1
    inA, inB = "11", "1"    # out: "100"
    solution = addBinary(inA,inB)
    print("test 1: " + solution)
    print("")
    # test 2
    inA, inB = "1010", "1011"   # out: "10101"
    solution = addBinary(inA,inB)
    print("test 2: " + solution)