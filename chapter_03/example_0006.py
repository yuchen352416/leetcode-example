#!/usr/bin/python3

from lib.ListLibraries import ListNode, ListInitialize


class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        dic = {}
        if head is None or head.next is None:
            return False
        while head is not None:
            if dic.get(head, 0) != 0:
                return True
            else:
                dic[head] = 1
            head = head.next
        return False

        # 哈希
        # dic = {}
        # node = head
        # while node:
        #     if dic.get(node, 0) != 0:
        #         return True
        #     else:
        #         dic[node] = 1
        #     node = node.next
        # return False

        # set 和字典一样
        # s = set()
        # node = head
        # while node:
        #     if node not in s:
        #         s.add(node)
        #     else:
        #         return True
        #     node = node.next
        # return False

        # 快慢指针
        # if not (head and head.next):
        #     return False
        # slow =head
        # quick = head.next
        # while quick and quick.next:
        #     if quick == slow:
        #         return True
        #     quick = quick.next.next
        #     slow = slow.next
        # return False
        # if not (head and head.next):
        #     return False
        # slow = head
        # quick = head.next
        # while quick and quick.next:
        #     if slow == quick:
        #         return True
        #     slow = slow.next
        #     quick = quick.next.next
        # return False


if __name__ == '__main__':
    flag = Solution().hasCycle(ListInitialize([1, 2, 3, 4, 5, 6, 7, 8, 9]).getCycleNode(-1))
    print(flag)
