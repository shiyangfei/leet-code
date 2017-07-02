#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two
#
# Easy (39.95%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
# 
# Given an integer, write a function to determine if it is a power of two.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # TODO: the problem did not define input as positive integer, so we have to consider negative nums
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            carry = n % 2
            if carry == 1:
                return False
            else:
                n = math.floor(n / 2)
        return True

