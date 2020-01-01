#!/usr/bin/python3

# 字符串转换整数
def myAtoi(s : str) -> int:
    res = 0
    symbol = 1
    s = s.strip()
    for i in range(0, len(s)):
        # 判断是否为数字
        asc = ord(s[i])
        if i == 0 and (asc == 43 or asc == 45):
            symbol = 44 - asc
            continue
        if 48 <= asc < 58:
            res = res * 10 + int(s[i])
        else:
            break
    res = res * symbol
    if res > 2 ** 31 - 1:
        res = 2 ** 31 - 1
    elif res < - 2 ** 31:
        res = - 2 ** 31
    return res
    # 大神写法
    # return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2 ** 31 - 1), -2 ** 31)


if __name__ == '__main__':
    result = myAtoi("   -42")
    # result = myAtoi("-91283472332")
    print(result)

