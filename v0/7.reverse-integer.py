#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer
#
# Easy (24.09%)
# Total Accepted:    234863
# Total Submissions: 974744
# Testcase Example:  '0'
#
# Reverse digits of an integer.
#
#
# Example1: x =  123, return  321
# Example2: x = -123, return -321
#
#
# click to show spoilers.
#
# Have you thought about this?
#
# Here are some good questions to ask before coding. Bonus points for you if
# you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such
# as 10, 100.
#
# Did you notice that the reversed integer might overflow? Assume the input is
# a 32-bit integer, then the reverse of 1000000003 overflows. How should you
# handle such cases?
#
# For the purpose of this problem, assume that your function returns 0 when the
# reversed integer overflows.
#
#
#
#
#
# Note:
# The input is assumed to be a 32-bit signed integer. Your function should
# return 0 when the reversed integer overflows.
#
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = 2 ** 31
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0
        while x > 0:
            result = (10 * result) + x % 10
            if result > max:
                return 0
            x //= 10
        return result * sign