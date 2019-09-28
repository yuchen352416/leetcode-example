#!/usr/bin/python3

# 两数之和
def twoSum(nums: list, target: int) -> list:
    # 笨办法: 效率太低了
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    for i in range(len(nums)):
        y = target - nums[i]
        if nums.__contains__(y):
            j = nums.index(y, 0)
            # 防止[3, 3] -> 6:这种情况
            if j != i:
                return [i, j]


if __name__ == '__main__':
    arr = [3, 3]
    print(arr)
    result = twoSum(arr, 6)
    print(result)
