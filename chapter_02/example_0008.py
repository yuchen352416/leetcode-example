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


if __name__ == '__main__':
    result = countAndSay(4)
    print(result)