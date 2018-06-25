#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers
#
# Easy (51.25%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# Example:
# Given a = 1 and b = 2, return 3.
# 
# 
# Credits:Special thanks to @fujiaozhu for adding this problem and creating all
# test cases.
#
class Solution(object):
    # TODO: need to understand binary operations

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        max_int = 0x7FFFFFFF
        mask = 0x100000000
        while b:
            holder = a
            a = (a ^ b) % mask
            b = ((holder & b) << 1) % mask
        result = a if a <= max_int else ~((a & max_int) ^ max_int)
        return result
