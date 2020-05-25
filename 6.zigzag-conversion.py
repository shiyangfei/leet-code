#
# @lc app=leetcode id=6 lang=python
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (34.58%)
# Total Accepted:    443.5K
# Total Submissions: 1.2M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        PLACE_HOLDER = 0
        matrix = []
        i = 0
        j = 0
        # could be right or bottom_left
        direction = 'right'
        for c_index in range(0, len(s)):
            c = s[c_index]
            # create place holder row
            if i > len(matrix) - 1:
                matrix.append([PLACE_HOLDER] * numRows)
            matrix[i][j] = c
            if j == 0:
                direction = 'right'
            if j == numRows - 1:
                direction = 'bottom_left'
            i = i if direction == 'right' else i + 1
            j = min(numRows - 1, j + 1) if direction == 'right' else max(0, j - 1)
        res = ''
        for col_index in range(0, numRows):
            for row in matrix:
                cell = row[col_index]
                if cell != PLACE_HOLDER:
                    res += cell
        return res

