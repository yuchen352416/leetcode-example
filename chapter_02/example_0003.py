#!/usr/bin/python3

# 字符串中的第一个唯一字符
def firstUniqChar(s: str) -> int:

    # container = {}
    # if len(s) == 0:
    #     return -1
    # elif len(s) == 1:
    #     return 0
    # else:
    #     for i in range(len(s)):
    #         if container.__contains__(s[i]):
    #             container[s[i]] += 1
    #         else:
    #             container[s[i]] = 0
    #     for key in container.keys():
    #         if container.get(key) == 0:
    #             return s.index(key)
    # return -1

    dic = {}
    for s1 in s:
        dic[s1] = dic.get(s1, 0) + 1
    for k, v in dic.items():
        if v == 1:
            return s.index(k)
    return -1



if __name__ == '__main__':
    result = firstUniqChar("left")
    print(result)
