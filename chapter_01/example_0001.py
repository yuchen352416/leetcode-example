#!/usr/bin/python3

# 从排序数组中删除重复项
def removeDuplicates(nums: list) -> int:
    indexs = []
    i = 0
    while nums.__len__() - 1 > i:
        if nums[i] == nums[i + 1]:
            indexs.append(i)
        i = i + 1

    i = indexs.__len__() - 1
    while i >= 0:
        nums.pop(indexs[i])
        i = i - 1

    print(indexs)
    print(nums)
    return nums.__len__()


if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 2, 3, 4]
    print(arr)
    l = removeDuplicates(arr)
    print(l)
