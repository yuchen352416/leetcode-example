#!/usr/bin/python3

#  实现 strStr()
def strStr(haystack: str, needle: str) -> int:
    res = 0
    if needle == "":
        return res
    return haystack.find(needle)

if __name__ == '__main__':
    result = strStr("baaaaaaaaaaaaaaaaaaa", "aa")
    print(result)

