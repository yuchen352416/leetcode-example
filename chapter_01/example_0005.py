#!/usr/bin/python3

# 只出现一次的数字
def singleNumber(nums: list) -> int:
    # nums.sort()
    # x = nums[0]
    # length = len(nums)
    # i = 1
    # while i < length:
    #     if x == nums[i]:
    #         x = nums[i + 1]
    #         i += 1
    #     i += 1
    #
    # return x

    x = 0
    for i in nums:
        x ^= i
    return x


if __name__ == '__main__':
    arr = [1, 1, 2, 2, 3]
    print(arr)
    result = singleNumber(arr)
    print(result)

