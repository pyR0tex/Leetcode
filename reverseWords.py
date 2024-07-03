# reverse each word in a string
s = "Let's take LeetCode contest" # out: "s'teL ekat edoCteeL tsetnoc"

def reverseWords(s : str) -> str:
    # sliced = s.split(' ')
    rList = []
    for slice in s.split(' '):
        rList.append(slice[::-1])
    return(' '.join(rList))

# approach2 good ol' one-liner
def reverseWords1(s : str) -> str:
    return ' '.join([slice[::-1] for slice in s.split(' ')])

def main():
    result = reverseWords(s)
    print(result)

    result1 = reverseWords1(s)
    print(result1)

if __name__ == '__main__':
    main()
