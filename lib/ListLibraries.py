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
            layer = [arr[: 0]]
            arr = arr[1:]
            i = 1
            # 分层
            while i < len(arr):
                print(pow(2, i))
                i += 1

    def getRoot(self) -> TreeNode:
        return self.root
