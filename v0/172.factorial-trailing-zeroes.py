#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes
#
# Easy (35.61%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ex = 1
        count_of_5 = 0
        while int(n / pow(5, ex)) >= 1:
            count_of_5 += int(n / pow(5, ex))
            ex += 1
        return count_of_5
