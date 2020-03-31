#!/usr/bin/python3

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxProfit = 0
        # l = len(prices)
        # if l < 2:
        #     return maxProfit
        # for i in range(0, l - 1):
        #     for j in range(i + 1, l):
        #         print("{}-{}={}".format(prices[j], prices[i], prices[j] - prices[i]))
        #         diff = prices[j] - prices[i]
        #         if diff > maxProfit:
        #             maxProfit = diff
        # return maxProfit
        pass


if __name__ == '__main__':
    # 简单的问候一下世界
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
