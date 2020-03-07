#!/usr/bin/python3

from lib.ListLibraries import TreeNode, TreeNodeInitialize


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        """
        type root: TreeNode
        rtype bool
        """
        if root is None or (root.left is None and root.right is None):
            return True
        if root.left is None or root.right is None:
            return False
        left = root.left
        right = root.right
        if left.val != right.val:
            return False
        return self.doublePointer(left, right)

    def doublePointer(self, left: TreeNode, right: TreeNode) -> bool:
        """
        type left: TreeNode
        type right: TreeNode
        rtype bool
        """
        # 外层判断
        if left.left is not None and right.right is not None:
            flag = self.doublePointer(left.left, right.right)
            if not flag or not left.val == right.val:
                return False

        elif left.left is None and right.right is None:
            flag = left.val == right.val
            if not flag:
                return False
        else:
            return False
        # 内层判断
        if left.right is not None and right.left is not None:
            flag = self.doublePointer(left.right, right.left)
            if not flag or not left.val == right.val:
                return False
        elif left.right is None and right.left is None:
            flag = left.val == right.val
            if not flag:
                return False
        else:
            return False
        return True


if __name__ == '__main__':
    root = TreeNodeInitialize([1, 2, 2, 3, 4, 4, 3]).getRoot()
    # root = TreeNodeInitialize([9, -42, -42, None, 76, 76, None, None, 13, None, 13]).getRoot()
    # root = TreeNode(1)
    # root.left = TreeNode(0)
    print(Solution().isSymmetric(root))
