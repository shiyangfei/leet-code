#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.90%)
# Total Accepted:    509K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
#
class Solution(object):
    # key is when the digit is 9
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = digits
        i = len(res) - 1
        carry = False
        is_first_run = True
        while i >= 0:
            curr_digit = res[i] + 1 if is_first_run else res[i]
            curr_digit = curr_digit + 1 if carry else curr_digit
            if curr_digit < 10:
                res[i] = curr_digit
                return res
            else:
                res[i] = curr_digit - 10
                carry = True
            is_first_run = False
            i -= 1
        if carry:
            res.insert(0, 1)
        return res

