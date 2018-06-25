#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four
#
# Easy (38.30%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '16'
#
# 
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example:
# Given num = 16, return true.
# Given num = 5, return false.
# 
# 
# Follow up: Could you solve it without loops/recursion?
# 
# Credits:Special thanks to @yukuairoy  for adding this problem and creating
# all test cases.
#
import math


class Solution(object):
    def helper(self, n):
        n = int(n)
        if n == 1:
            return True
        else:
            carry = n % 4
            if carry != 0:
                return False
            else:
                return self.helper(math.floor(n / 4))

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        return self.helper(num)
