#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number
#
# Easy (46.44%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"A"'
#
# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length_s = len(s)
        index_s = length_s - 1
        num = 0
        while index_s >= 0:
            char = s[index_s]
            ex = length_s - 1 - index_s
            unit_num = (ord(char) - ord('A') + 1) * pow(26, ex)
            num += unit_num
            index_s -= 1
        return num
