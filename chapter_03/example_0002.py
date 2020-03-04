#!/usr/bin/python3

from lib.ListLibraries import ListNode, ListNodeInitialize


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = ListNode(0)
        first.next = head
        second = ListNode(0)
        second.next = head
        # 第一个指针先走步
        for i in range(n):
            if first.next:
                first = first.next
            else:
                return None
        # 如果first指针走到头, 说明要删的是头结点，用头结点的下一个作为返回值即可
        if first.next is None:
            return head.next
        # 两个指针同时走
        while first.next:
            first = first.next
            second = second.next
        # 删除
        second.next = second.next.next
        return head


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    # arr = [1]
    init = ListNodeInitialize(arr)
    node = Solution().removeNthFromEnd(init.getNode(), 5)
    print(init.getArray(node))


