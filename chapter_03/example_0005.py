#!/usr/bin/python3

from lib.ListLibraries import ListNode, ListInitialize


class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        if head is None:
            return True
        while head:
            arr.append(head.val)
            head = head.next

        i = 0
        flag = True
        while i <= len(arr) // 2 and flag:
            flag = arr[i] == arr[-i - 1]
            i += 1
        return flag


if __name__ == '__main__':
    flag = Solution().isPalindrome(ListInitialize([1]).getNode())
    print(flag)
