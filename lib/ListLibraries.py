#!/usr/bin/python3

from typing import List
from math import pow


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeInitialize:

    def __init__(self, arr: List[int]):
        if len(arr) == 0:
            self.node = None
        else:
            nodes: List[ListNode] = []
            self.node = ListNode(arr[0])
            nodes.append(self.node)
            for i in range(1, len(arr)):
                nodes.append(ListNode(arr[i]))
                nodes[i - 1].next = (nodes[i])

    def getNode(self) -> ListNode:
        return self.node

    def getCycleNode(self, pos: int) -> ListNode:
        temp = self.node
        i = 0
        circuit = None
        while temp.next is not None:
            if pos == i:
                circuit = temp
            temp = temp.next
            i += 1
        temp.next = circuit
        return self.node

    def getArray(self, node: ListNode) -> List:
        arr = []
        if node:
            while node.next:
                arr.append(node.val)
                node = node.next
            arr.append(node.val)
        return arr


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeNodeInitialize:

    def __init__(self, arr: List[int]):
        if len(arr) == 0:
            self.root = None
        else:
            self.root = TreeNode(arr[0])
            index = [0, 1]
            i = 1
            # 树的每层节点
            treeLayerNodes = [self.root]
            while index[1] < len(arr):
                index[0] = index[1]
                index[1] = index[0] + int(pow(2, i))
                treeLayerNodes.append(arr[index[0]: index[1]])
                i += 1

            for i in range(1, len(treeLayerNodes)):
                # 遍历每层节点
                j = 0
                while j < len(treeLayerNodes[i]):
                    treeNodeIndex = j // 2
                    if treeLayerNodes[i][j] is None:
                        left = None
                    else:
                        left = TreeNode(treeLayerNodes[i][j])

                    if treeLayerNodes[i][j + 1] is None:
                        right = None
                    else:
                        right = TreeNode(treeLayerNodes[i][j + 1])
                    if i == 1:
                        upperLayerNode = treeLayerNodes[0]
                    else:
                        upperLayerNode = treeLayerNodes[i - 1][treeNodeIndex]
                    if upperLayerNode is not None:
                        upperLayerNode.left = left
                        upperLayerNode.right = right
                    treeLayerNodes[i][treeNodeIndex] = left
                    treeLayerNodes[i][treeNodeIndex + 1] = right

                    j += 2

    def getRoot(self) -> TreeNode:
        return self.root
