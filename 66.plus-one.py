#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one
#
# Easy (37.87%)
# Total Accepted:    161956
# Total Submissions: 427575
# Testcase Example:  '[0]'
#
# Given a non-negative integer represented as a non-empty array of digits, plus
# one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        carry = 0
        index = length - 1
        while index >= 0:
            digit = digits[index]
            if index == length - 1:
                sum_val = digit + 1 + carry
            else:
                sum_val = digit + carry
            val = sum_val if sum_val < 10 else sum_val % 10
            carry = 0 if sum_val < 10 else 1
            digits[index] = val
            index -= 1
        if carry == 1:
            digits.insert(0, carry)
        return digits
