#!/usr/bin/python3

from lib.ListLibraries import TreeNode, TreeNodeInitialize


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        layerNodes = [root]
        layerNumber = 1
        flag = True
        while flag:
            tempLayerNodes = []
            for tree in layerNodes:
                if tree.left is not None and tree.left.val is not None:
                    tempLayerNodes.append(tree.left)
                if tree.right is not None and tree.right.val is not None:
                    tempLayerNodes.append(tree.right)
                layerNodes = tempLayerNodes
            if len(layerNodes) > 0:
                layerNumber += 1
            else:
                flag = False
        return layerNumber
        # 大神写的
        # if root is None:
        #     return 0
        # 递归的方法实现
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    # 简单的问候一下世界
    root = TreeNodeInitialize([3, 9, 20, None, None, 15, 7]).getRoot()
    print(Solution().maxDepth(root))
