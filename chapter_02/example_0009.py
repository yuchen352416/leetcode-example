#!/usr/bin/python3

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    '''
    最长公共前缀
    '''
    result = ""
    i = 0
    while True:
        represent = ""
        try:
            represent = strs[0][i]
            for k in range(1, len(strs)):
                if represent != strs[k][i]:
                    return result
        except Exception:
            return result
        i = i + 1
        result = result + represent


if __name__ == '__main__':
    result = longestCommonPrefix(["flower", "flow", "flight", ""])
    print(result)
