#!/usr/bin/python3

# 验证回文字符串
def isPalindrome(s: str) -> bool:
    arr = []
    s = s.lower()
    for x in s:
        if 'a' <= x <= 'z' or '0' <= x <= '9':
            arr.append(x)
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr) - (i+1)]:
            return False
    return True


if __name__ == '__main__':
    result = isPalindrome("A man, a plan, a canal: Panama")
    print(result)

