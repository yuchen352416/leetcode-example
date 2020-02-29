#!/usr/bin/python3

from lib.ListLibraries import ListNode, ListInitialize


class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        pass


if __name__ == '__main__':
    flag = Solution().hasCycle(ListInitialize([1]).getNode())
    print(flag)
