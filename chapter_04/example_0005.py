#!/usr/bin/python3

from lib.ListLibraries import TreeNode
from typing import List


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        type nums: List[int]
        rtype TreeNode
        """
        l = len(nums)
        if l == 0:
            return None
        if l == 1:
            return TreeNode(nums[0])
        elif l <= 3:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            if l == 3:
                root.right = TreeNode(nums[2])
            else:
                root.right = None
            return root
        else:
            # 中位数
            median = int(l / 2)
            root = TreeNode(nums[median])
            root.left = self.sortedArrayToBST(nums[:median])
            root.right = self.sortedArrayToBST(nums[median + 1:])
            return root


if __name__ == '__main__':
    root = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    print(root)
