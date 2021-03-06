#!/usr/bin/python3

from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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

        minPrice = sys.maxsize
        maxProfit = 0
        for x in prices:
            if x < minPrice:
                minPrice = x
            elif x - minPrice > maxProfit:
                maxProfit = x - minPrice
        return maxProfit


if __name__ == '__main__':
    # 简单的问候一下世界
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
