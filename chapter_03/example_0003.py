#!/usr/bin/python3

from lib.ListLibraries import ListNode, ListInitialize


class Solution:

    def __init__(self):
        self.node = None

    def reverseList(self, head) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            self.reverseList(head.next)
            current = ListNode(head.val)
            tempNode = self.node
            while tempNode.next:
                tempNode = tempNode.next
            tempNode.next = current
            return self.node
        else:
            if head:
                self.node =ListNode(head.val)
                return self.node
            else:
                return None
        # 大佬写的
        # if head == None or head.next == None:
        #     return head
        # cur = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return cur


if __name__ == '__main__':
    # arr = [1, 2, 3, 4, 5]
    arr = []
    init = ListInitialize(arr)
    node = Solution().reverseList(init.getNode())
    print(init.getArray(node))


