#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (48.72%)
# Total Accepted:    250.6K
# Total Submissions: 514.4K
# Testcase Example:  '"III"'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
# 
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
# 
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# 
# Given a roman numeral, convert it to an integer. Input is guaranteed to be
# within the range from 1 to 3999.
# 
# Example 1:
# 
# 
# Input: "III"
# Output: 3
# 
# Example 2:
# 
# 
# Input: "IV"
# Output: 4
# 
# Example 3:
# 
# 
# Input: "IX"
# Output: 9
# 
# Example 4:
# 
# 
# Input: "LVIII"
# Output: 58
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
# 
# 
# Example 5:
# 
# 
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
#
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_map = {
            'I': {
                'value': 1,
                'unit_5': 'V',
                'unit_10': 'X'
            },
            'V': {
                'value': 5
            },
            'X': {
                'value': 10,
                'unit_5': 'L',
                'unit_10': 'C'
            },
            'L': {
                'value': 50
            },
            'C': {
                'value': 100,
                'unit_5': 'D',
                'unit_10': 'M'
            },
            'D': {
                'value': 500
            },
            'M': {
                'value': 1000
            }
        }
        res = 0
        i = 0
        while True:
            if i == len(s):
                break
            c = s[i]
            unit = num_map[c]
            value = unit.get('value')
            if i + 1 < len(s):
                next_c = s[i + 1]
                if unit.get('unit_5') == next_c:
                    res += value * 4
                    i += 2
                    continue
                if unit.get('unit_10') == next_c:
                    res += value * 9
                    i += 2
                    continue
            res += value
            i += 1
        return res
