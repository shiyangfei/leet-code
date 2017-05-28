#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx
#
# Easy (27.49%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x.
#

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left = 1
        right = x
        while left + 1 < right:
            mid = (left + right) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid
            else:
                right = mid
        if right * right <= x:
            return right
        else:
            return left
