# 168. Excel Sheet Column Title

def ConvertToTitle(columnNumber: int) -> str:
    print("     -- Excel Column Title --\n")
    result = ""
    n = columnNumber
    while n > 0:
        n -= 1
        result += (chr(ord('A') + n%26))
        n //= 26
    return result[::-1]


if __name__ == '__main__':
    columnNumber = 130
    result = ConvertToTitle(columnNumber)
    print(f"        Result: {result}")

