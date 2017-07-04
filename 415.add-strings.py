#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings
#
# Easy (41.24%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length1 = len(num1)
        length2 = len(num2)
        if length1 == 0:
            return num2
        if length2 == 0:
            return num1
        list1 = list(num1)
        list2 = list(num2)
        diff = length1 - length2
        if diff > 0:
            list2 = ['0'] * diff + list2
        if diff < 0:
            list1 = ['0'] * (0 - diff) + list1
        length = max(length1, length2)
        result = ['0'] * length
        carry = 0
        for i in range(length):
            index = length - 1 - i
            val = carry + int(list1[index]) + int(list2[index])
            if val >= 10:
                val = val - 10
                carry = 1
            else:
                carry = 0
            result[index] = str(val)
        if carry == 1:
            result.insert(0, str(1))
        return ''.join(result)

# Solution().addStrings('9', '99')
