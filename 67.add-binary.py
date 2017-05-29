#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary
#
# Easy (31.71%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"0"\n"0"'
#
# 
# Given two binary strings, return their sum (also a binary string).
# 
# 
# 
# For example,
# a = "11"
# b = "1"
# Return "100".
# 
#

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        length = max(len_a, len_b)
        fill_a = '0' * (length - len_a)
        a = fill_a + a
        fill_b = '0' * (length - len_b)
        b = fill_b + b
        i = length - 1
        carry = 0
        result = ""
        while i >= 0:
            val_a = int(a[i])
            val_b = int(b[i])
            val = val_a + val_b + carry
            if val == 0:
                val = 0
                carry = 0
            if val == 1:
                val = 1
                carry = 0
            if val == 2:
                val = 0
                carry = 1
            if val == 3:
                val = 1
                carry = 1
            result = str(val) + result
            i -= 1
        if carry == 1:
            result = '1' + result
        return result
