# reverses an array of characters in place. O(1) auxillary space given

s = ["h","e","l","l","o"] # output: ["o","l","l","e","h"]
s1 = ["h","e","l","l","o"] # output: ["o","l","l","e","h"]
s2 = ["h","e","l","l","o"] # output: ["o","l","l","e","h"]
# works, could be faster I believe
def reverseString(s : list[str]) -> None:
    i, j = 0, len(s) - 1
    while(i < j):
        s[i],s[j] = s[j],s[i]
        i += 1; j -= 1

# approach2; good ol' one-liner
def reverseString1(s : list[str]) -> None:
    s.reverse()

# approach3: another good ol' ine-liner
def reverseString2(s : list[str]) -> None:
    s[:] = s[::-1]

def main():
    reverseString(s)
    print(s)

    reverseString1(s1)
    print(s1)

    reverseString2(s2)
    print(s2)


if __name__ == '__main__':
    main()
