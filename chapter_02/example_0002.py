#!/usr/bin/python3

import math


# 整数反转
def reverse(x: int) -> int:
    result = 0
    flag = 0
    if x < 0:
        x = -x
        flag = 1

    while x > 0:
        result = (result * 10) + (x % 10)
        x = x // 10

    if flag == 1:
        result = -result

    if result > 2147483647 or result < math.pow(-2, 31):
        return 0
    return result


if __name__ == '__main__':
    x = 1534236469
    result = reverse(x)
    print(result)
