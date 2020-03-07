#!/usr/bin/python3

from lib.ListLibraries import TreeNode, TreeNodeInitialize
from typing import List


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        # (1)错误的想法: 这个结构, 只能判断当前节点, 是否符合二叉搜索树, 不能判断当前节点在整个树中, 是否符合.
        # eg: [10, 5, 15, None, None, 6, 20]中, 6 虽然小于15 但6不大于10
        # if root is None:
        #     return True
        # if root.left is None and root.right is None:
        #     return True
        # flag = self.isValidBST(root.left) and self.isValidBST(root.right)
        # if root.left is not None and root.right is not None:
        #     flag = flag and root.left.val < root.val < root.right.val
        # elif root.left is not None:
        #     flag = flag and root.left.val < root.val
        # else:
        #     flag = flag and root.val < root.right.val
        # return flag

        if root is None:
            return True
        arr = self.treeToArray(root)
        if len(arr) == 1:
            return True
        i = 1
        while i < len(arr):
            if arr[i - 1] >= arr[i]:
                return False
            i += 1
        return True
    # 大神写的
    #     def effective(node, low=float("-inf"), high=float("inf")):
    #         if not node:
    #             return True
    #         val = node.val
    #         if val <= low or val >= high:
    #             return False
    #         if not effective(node.left, low, val):
    #             return False
    #         if not effective(node.right, val, high):
    #             return False
    #         return True
    #     return effective(root)

    def treeToArray(self, root: TreeNode) -> List:
        """
        type root: TreeNode
        rtype List[int]
        """
        arr = []
        if root.left is not None:
            tempLeftArray = self.treeToArray(root.left)
            for i in tempLeftArray:
                arr.append(i)
        arr.append(root.val)
        if root.right is not None:
            tempRightArray = self.treeToArray(root.right)
            for i in tempRightArray:
                arr.append(i)
        return arr




if __name__ == '__main__':
    root = TreeNodeInitialize([5, 1, 7, None, None, 6, 8]).getRoot()
    # root = TreeNode(0)
    # root.left = TreeNode(-1)
    print(Solution().isValidBST(root))
