#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman
#
# Medium (43.88%)
# Total Accepted:    101562
# Total Submissions: 231440
# Testcase Example:  '1'
#
# Given an integer, convert it to a roman numeral.
# 
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rest = num
        checks = get_checks()
        result = ''
        for check in checks:
            unit = check['unit']
            val = rest // unit
            char = get_char(val, check)
            result = result + char
            rest %= unit
        return result


def get_char(val, check):
    if val == 9:
        return check['char'] + check['ten_time_char']
    if val == 5:
        return check['five_time_char']
    if val == 4:
        return check['char'] + check['five_time_char']
    else:
        if val > 5:
            return check['five_time_char'] + check['char'] * (val - 5)
        else:
            return check['char'] * val


def get_checks():
    return [
        {
            'unit': 1000,
            'char': 'M',
            'five_time_char': None,
            'ten_time_char': None
        },
        {
            'unit': 100,
            'char': 'C',
            'five_time_char': 'D',
            'ten_time_char': 'M'
        },
        {
            'unit': 10,
            'char': 'X',
            'five_time_char': 'L',
            'ten_time_char': 'C'
        },
        {
            'unit': 1,
            'char': 'I',
            'five_time_char': 'V',
            'ten_time_char': 'X'
        }
    ]
