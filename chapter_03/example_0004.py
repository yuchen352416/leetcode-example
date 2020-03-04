#!/usr/bin/python3

from lib.ListLibraries import ListNode, ListNodeInitialize


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        i = 0
        first = None
        tempNode = None
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    node = ListNode(l1.val)
                    l1 = l1.next
                else:
                    node = ListNode(l2.val)
                    l2 = l2.next
            elif l1 is None:
                node = l2
                l2 = l2.next
            else:
                node = l1
                l1 = l1.next

            if i == 0:
                first = node
                tempNode = node
            else:
                tempNode.next = node
                tempNode = tempNode.next
            i += 1
        return first


if __name__ == '__main__':
    l1 = ListNodeInitialize([1, 2, 6])
    l2 = ListNodeInitialize([1, 3, 4, 5, 7, 8, 9])
    node = Solution().mergeTwoLists(l1.getNode(), l2.getNode())
    print(ListNodeInitialize([]).getArray(node))


