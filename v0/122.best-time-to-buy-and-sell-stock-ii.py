#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
#
# Easy (46.45%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times). However, you may not engage in multiple transactions at the
# same time (ie, you must sell the stock before you buy again).
#
import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        low = sys.maxsize
        high = None
        for i in range(0, len(prices)):
            if high is None and prices[i] < low:
                low = prices[i]
                continue
            if prices[i] > low and prices[i] > high:
                high = prices[i]
                continue
            if low < high:
                profit = high - low
                result += profit
                low = prices[i]
                high = None
        result += (high - low) if (high is not None and (high - low) > 0) else 0
        return result


Solution().maxProfit([1, 4, 2])
