#!/usr/bin/python3

from lib.ListLibraries import ListNode, ListInitialize


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    node = ListInitialize([1, 2, 3, 4, 5]).getNode()
    print(node.getArray())


