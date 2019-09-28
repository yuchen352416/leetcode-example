#!/usr/bin/python3

# 加一
def plusOne(digits: list) -> list:
    i = len(digits) - 1
    while i >= 0:
        if digits[i] == 9:
            digits[i] = 0
            i -= 1
        else:
            digits[i] += 1
            return digits

    if i < 0:
        digits.insert(0, 1)
    return digits


if __name__ == '__main__':
    arr = [9]
    print(arr)
    result = plusOne(arr)
    print(result)
