#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (27.85%)
# Total Accepted:    218.7K
# Total Submissions: 785.2K
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
    def add_to_row(self, row, index, value):
        while len(row) < index:
            row.append(None)
        if len(row) == index:
            row.append(value)
        else:
            row[index] = value

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == '' or numRows == 1:
            return s
        matrix = list()
        for i in range(0, numRows):
            row = list()
            matrix.append(row)
        direction = 'down'
        position = None
        for i, c in enumerate(s):
            if position is None:
                position = dict(x=0, y=0)
            elif direction == 'down':
                position['y'] += 1
            else:
                position['x'] += 1
                position['y'] -= 1
            target_row = matrix[position['y']]
            self.add_to_row(target_row, position['x'], c)
            if direction == 'down' and position['y'] == numRows - 1:
                direction = 'up'
            if direction == 'up' and position['y'] == 0:
                direction = 'down'
        result = ''
        for row in matrix:
            for c in row:
                if c is not None:
                    result += c
        return result
