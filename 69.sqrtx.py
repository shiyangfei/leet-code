#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (32.79%)
# Total Accepted:    477.6K
# Total Submissions: 1.5M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
class Solution(object):
    # use dichotomy to optimize the performance
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        res = 0
        while left < right:
            if left * left < x < right * right:
                if left == right - 1:
                    return left
                mid = int((left + right) / 2)
                if mid * mid > x:
                    right = mid
                elif mid * mid < x:
                    left = mid
                else:
                    return mid
            elif left * left == x:
                return left
            else:
                return right
        return res
