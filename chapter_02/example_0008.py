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
        result = ""
        s = countAndSay(n - 1)
        maps = {}
        for i in range(len(s)):
            keys = list(maps.keys())
            key = ""
            if len(keys) == 1:
                key = keys[0]
            if key == s[i]:
                maps[key] = maps.get(key) + 1
            else:
                val = maps.get(key, "")
                result = result + val.__str__() + key
                maps.clear()
                maps[s[i]] = 1
        result = result + list(maps.values())[0].__str__() + list(maps.keys())[0].__str__()
        return result
    # 大神写的
    # s = '1'
    # for i in range(2, n + 1):
    #     ls = []
    #     i = 0
    #     l = len(s)
    #     for j in range(l + 1):
    #         if j == l or s[j] != s[i]:
    #             ls.append(str(j - i) + s[i])
    #             i = j
    #     s = ''.join(ls)
    # return s


if __name__ == '__main__':
    result = countAndSay(4)
    print(result)
