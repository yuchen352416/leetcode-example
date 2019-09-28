#!/usr/bin/python3

# 移零
def moveZeroes(nums: list) -> list:
    # 改变了数组内, 非零元素的位置
    # zeroCount = 1
    # i = 0
    # while i < len(nums):
    #     if nums[i] == 0:
    #         if nums[len(nums) - zeroCount] != 0:
    #             nums[i] = nums[len(nums) - zeroCount]
    #             nums[len(nums) - zeroCount] = 0
    #         else:
    #             i -= 1
    #         zeroCount += 1
    #     i += 1
    #     if i + zeroCount > len(nums):
    #         break
    # return nums

    zeroCount = 1
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            if nums[len(nums) - zeroCount] != 0:
                nums.pop(i)
                nums.append(0)
                i -= 1
            else:
                i -= 1
            zeroCount += 1
        i += 1
        if i + zeroCount > len(nums):
            break
    return nums

if __name__ == '__main__':
    arr = [0, 0, 1]
    print(arr)
    result = moveZeroes(arr)
    print(result)
