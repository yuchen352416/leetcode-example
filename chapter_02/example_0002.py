#!/usr/bin/python3

# 整数反转
def reverseString(s: list) -> None:
    l = s.__len__()
    for i in range(l // 2):
        s[i], s[l - i - 1] = s[l - i - 1], s[i]



if __name__ == '__main__':
    arr = ["h", "e", "l", "l", "o"]
    print(arr)
    reverseString(arr)
    print(arr)
