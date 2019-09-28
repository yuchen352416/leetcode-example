#!/usr/bin/python3

# 两个数组的交集
def intersect(nums1: list, nums2: list) -> list:
    # 双指针法
    nums1.sort()
    nums2.sort()
    i = 0
    j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result


if __name__ == '__main__':
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]
    print(arr1)
    print(arr2)
    result = intersect(arr1, arr2)
    print(result)
