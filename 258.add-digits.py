#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits
#
# Easy (50.96%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# 
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit. 
# 
# 
# 
# For example:
# 
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
# one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
import math


class Solution(object):
    def get_answer(self, num):
        digits = self.get_digits(num)
        if len(digits) == 1:
            return int(digits[0])
        else:
            new_num = 0
            for index, digit in enumerate(digits):
                new_num += digit
            return self.get_answer(new_num)

    def get_digits(self, num):
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = math.floor(num / 10)
        return digits

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        else:
            return self.get_answer(num)
