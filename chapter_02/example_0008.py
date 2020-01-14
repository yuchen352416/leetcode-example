#!/usr/bin/python3


def countAndSay(n: int) -> str:
    '''
    外观数列
    '''
    if n < 1:
        return ""
    if n == 1:
        return "1"
    else:
        maps = {}
        s = countAndSay(n - 1)
        for i in range(len(s) - 1):
            if maps.__contains__(s[i]):
                maps[s[i]] = maps.get(s[i], 0) + 1
            else:
                maps[s[i]] = 1
        return "11"


if __name__ == '__main__':
    result = countAndSay(5)
    print(result)