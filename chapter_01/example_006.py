#!/usr/bin/python3

# 两个数组的交集
def intersect(nums1: list, nums2: list) -> list:
    # 双指针法
    nums1.sort()
    nums2.sort()
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        pass

    return None


if __name__ == '__main__':
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]
    print(arr1)
    print(arr2)
    result = intersect(arr1, arr2)
    print(result)
