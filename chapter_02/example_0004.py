#!/usr/bin/python3


# 有效的字母异位词
def isAnagram(s: str, t: str) -> bool:
    dictA = {}
    dictB = {}
    if len(s) != len(t):
        return False
    else:
        for i in range(len(s)):
            dictA[s[i]] = dictA.get(s[i], 0) + 1
            dictB[t[i]] = dictB.get(t[i], 0) + 1
        for k, v in dictA.items():
            if v != dictB.get(k, 0):
                return False
        return True


if __name__ == '__main__':
    result = isAnagram("anagram", "nagaram")
    print(result)
