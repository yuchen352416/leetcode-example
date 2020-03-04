#!/usr/bin/python3

from lib.ListLibraries import ListNode, ListNodeInitialize


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    node = ListNodeInitialize([4, 5, 1, 9]).getNode()
    deleteNode = node
    while deleteNode.val != 1:
        deleteNode = deleteNode.next
    Solution().deleteNode(deleteNode)
    print(deleteNode.val)

