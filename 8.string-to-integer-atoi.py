#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (14.13%)
# Total Accepted:    244.7K
# Total Submissions: 1.7M
# Testcase Example:  '"42"'
#
# Implement atoi which converts a string to an integer.
# 
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
# 
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned.
# 
# Note:
# 
# 
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical
# value is out of the range of representable values, INT_MAX (231 − 1) or
# INT_MIN (−231) is returned.
# 
# 
# Example 1:
# 
# 
# Input: "42"
# Output: 42
# 
# 
# Example 2:
# 
# 
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus
# sign.
# Then take as many numerical digits as possible, which gets 42.
# 
# 
# Example 3:
# 
# 
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a
# numerical digit.
# 
# 
# Example 4:
# 
# 
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a
# numerical 
# digit or a +/- sign. Therefore no valid conversion could be performed.
# 
# Example 5:
# 
# 
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed
# integer.
# Thefore INT_MIN (−231) is returned.
# 
#
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        is_neg = False
        str_start = False
        num_start = False
        res = 0
        max_high = 2 ** 31 - 1
        max_low = -(2 ** 31)
        for c in str:
            if c == ' ' and not str_start:
                continue
            if c != ' ' and not str_start:
                str_start = True
            # if first c is not valid, return 0
            if c != '+' and c != '-' and (c < '0' or c > '9'):
                break
            if not num_start:
                if c == '-':
                    is_neg = not is_neg
                    num_start = True
                    continue
                if c == '+':
                    num_start = True
                    continue
                if '0' <= c <= '9':
                    num_start = True
            if num_start:
                if not '0' <= c <= '9':
                    break
                else:
                    res = res * 10 + int(c)
                    num_start = True
        res = res if not is_neg else -res
        res = max_high if res > max_high else res
        res = max_low if res < max_low else res
        return res
