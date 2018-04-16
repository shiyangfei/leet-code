#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (35.82%)
# Total Accepted:    321.3K
# Total Submissions: 896.9K
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Could you solve it without converting the integer to a string?
# 
#
import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        digits = list()
        num = x
        while num > 0:
            digit = int(num % 10)
            num = math.floor(num / 10)
            digits.append(digit)
        length = len(digits)
        left_index = 0
        right_index = length - 1
        while left_index < right_index:
            if digits[left_index] != digits[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True
