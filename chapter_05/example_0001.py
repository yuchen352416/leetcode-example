#!/usr/bin/python3

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        description: 合并两个有序数组
        type nums1: List[int]
        type m: int
        type nums2: List[int]
        type n: int
        rtype: None
        """
        if len(nums1) == 0:
            for x in nums2[:n]:
                nums1.append(x)
            return
        if len(nums2) == 0:
            tempNums1 = nums1[:m]
            nums1.clear()
            for x in tempNums1:
                nums1.append(x)
            return
        tempNums1 = nums1.copy()
        i = 0
        j = 0
        nums1.clear()
        while i < m or j < n:
            if i < m and (j == n or tempNums1[i] < nums2[j]):
                nums1.append(tempNums1[i])
                i += 1
            elif j < n:
                nums1.append(nums2[j])
                j += 1
        # 大神写的(这tm就看不懂了)
        # nums1[m:m + n] = nums2
        # nums1.sort()


if __name__ == '__main__':
    # 简单的问候一下世界
    nums1 = [2, 0]
    nums2 = [1]
    m = 1
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
