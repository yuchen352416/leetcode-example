#!/usr/bin/python3

from lib.ListLibraries import ListNode, ListInitialize


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
        while l1.next is None and l2.next is None:
            if l1.val < l2.val:
                node = ListNode(l1.val)
            else:
                node = ListNode(l2.val)





if __name__ == '__main__':
    l1 = ListInitialize([1, 2, 4])
    l2 = ListInitialize([1, 3, 4])
    node = Solution().mergeTwoLists(l1, l2)
    print(ListInitialize([]).getArray(node))


