#!/usr/bin/python3

from lib.ListLibraries import TreeNode, TreeNodeInitialize
from typing import List


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        type root: TreeNode
        rtype List
        """
        if root is None:
            return []
        treeNodes = [root]
        valueArray = []
        while len(treeNodes) > 0:
            tempTreeNodes = []
            itemValue = []
            for tree in treeNodes:
                if tree.left is not None:
                    tempTreeNodes.append(tree.left)
                if tree.right is not None:
                    tempTreeNodes.append(tree.right)
                itemValue.append(tree.val)
            valueArray.append(itemValue)
            treeNodes = tempTreeNodes
        return valueArray


if __name__ == '__main__':
    root = TreeNodeInitialize([1, 2, 2, 3, 4, 4, 3]).getRoot()
    # root = TreeNodeInitialize([9, -42, -42, None, 76, 76, None, None, 13, None, 13]).getRoot()
    # root = TreeNode(1)
    # root.left = TreeNode(0)
    print(Solution().levelOrder(root))
