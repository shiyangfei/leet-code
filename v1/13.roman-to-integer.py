#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (48.07%)
# Total Accepted:    224.7K
# Total Submissions: 467.4K
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
        result = 0
        value_map = dict(
            M=1000,
            CM=900,
            D=500,
            CD=400,
            C=100,
            XC=90,
            L=50,
            XL=40,
            X=10,
            IX=9,
            V=5,
            IV=4,
            III=3,
            II=2,
            I=1,
        )
        roman = s
        while len(roman) > 0:
            for key in value_map:
                num = value_map[key]
                if roman.find(key) == 0:
                    result += num
                    roman = roman[len(key):]

        return result
