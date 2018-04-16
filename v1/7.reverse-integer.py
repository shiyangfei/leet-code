#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.37%)
# Total Accepted:    396.4K
# Total Submissions: 1.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
# 
#
import math


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = x < 0
        num = math.fabs(x)
        result = 0
        high_limit = 2 ** 31 - 1
        low_limit = 2 ** 31
        while num > 0:
            digit = num % 10
            result = result * 10 + digit
            if result >= high_limit:
                return 0
            if is_neg is True and result >= low_limit:
                return 0
            num = math.floor(num / 10)
        result = int(result) if not is_neg else 0 - int(result)
        return result
