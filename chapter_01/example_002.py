#!/usr/bin/python3

# 买卖股票的最佳时机2
def maxProfit(prices: list) -> int:
    if prices.__len__() < 2: return 0
    sum = 0
    for i in range(prices.__len__() - 1):
        if prices[i] < prices[i + 1]:
            sum += prices[i + 1] - prices[i]
    return sum



if __name__ == '__main__':
    # arr = [7, 1, 5, 3, 6, 4]
    # arr = [6, 1, 3, 2, 4, 7]
    # arr = [1, 2, 3, 4, 5]
    arr = [3, 3, 5, 0, 0, 3, 1, 4]
    print(arr)
    p = maxProfit(arr)
    print(p)



