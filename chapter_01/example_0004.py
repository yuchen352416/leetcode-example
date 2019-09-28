#!/usr/bin/python3

# 存在重复
def containsDuplicate(nums: list) -> bool:
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(arr)
    flag = containsDuplicate(arr)
    print(flag)
