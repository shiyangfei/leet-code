#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three
#
# Easy (40.02%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '27'
#
# 
# ⁠   Given an integer, write a function to determine if it is a power of
# three.
# 
# 
# ⁠   Follow up:
# ⁠   Could you do it without using any loop / recursion?
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
import math


class Solution(object):
    def helper(self, n):
        n = int(n)
        if n == 1:
            return True
        else:
            carry = n % 3
            if carry != 0:
                return False
            else:
                return self.helper(math.floor(n / 3))

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1 or n == 3:
            return True
        return self.helper(n)
