#!/usr/bin/python3

class Solution:
    def isBadVersion(self, version: int) -> bool:
        if version >= 20:
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
        pass


if __name__ == '__main__':
    # 简单的问候一下世界
    print(Solution().firstBadVersion(100))
