#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer
#
# Easy (44.80%)
# Total Accepted:    143645
# Total Submissions: 320604
# Testcase Example:  '"DCXXI"'
#
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sub_map = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        result = 0
        length = len(s)
        i = 0
        while i < length:
            c = s[i]
            if (i + 1) < length:
                next_c = s[(i + 1)]
                if (c + next_c) in sub_map:
                    result += sub_map[(c + next_c)]
                    i += 2
                    continue
            if c in c_map:
                result += c_map[c]
                i += 1
        return result


Solution().romanToInt('DCXXI')
