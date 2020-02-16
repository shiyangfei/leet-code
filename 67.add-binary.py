#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (42.07%)
# Total Accepted:    386.6K
# Total Submissions: 917.1K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution(object):
    @staticmethod
    # returns val, carry
    def calc(a, b, carry):
        if a + b + carry == 0:
            return 0, 0
        if a + b + carry == 1:
            return 1, 0
        if a + b + carry == 2:
            return 0, 1
        if a + b + carry == 3:
            return 1, 1
        raise Exception('invalid input for calc func')

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        a_len = len(a)
        b_len = len(b)
        i = 1
        carry = 0
        while True:
            a_index = a_len - i
            b_index = b_len - i
            if a_index < 0 and b_index < 0 and carry == 0:
                break
            a_curr = int(a[a_index]) if a_index >= 0 else 0
            b_curr = int(b[b_index]) if b_index >= 0 else 0
            val, carry = self.calc(a_curr, b_curr, carry)
            res = str(val) + res
            i += 1
        return res
