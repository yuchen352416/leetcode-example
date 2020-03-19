#!/usr/bin/python3

class Solution:
    def isBadVersion(self, version: int) -> bool:
        if version >= 2:
            return True
        else:
            return False

    def firstBadVersion(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        # 效率太低了
        # for i in range(n + 1):
        #     flag = self.isBadVersion(i)
        #     if flag:
        #         return i
        left = 1
        right = n
        while right > left:
            m = int((right - left) / 2 + left)
            print("m: {0}, start: {1}, end: {2}".format(m, left, right))
            if self.isBadVersion(m):
                right = m
            else:
                left = m + 1
        return left


if __name__ == '__main__':
    # 简单的问候一下世界
    print(Solution().firstBadVersion(3))
