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
        if numRows <= 1:
            return s
        gaps = [1 + (numRows - 2) * 2, -1]
        res = ''
        row_index = 0
        while gaps[0] >= -1:
            gap_index = 0
            skip = False
            cur_index = row_index
            while cur_index < len(s):
                if not skip:
                    res += s[cur_index]
                gap = gaps[gap_index]
                gap_index = 1 if gap_index == 0 else 0
                if gap > 0:
                    cur_index = cur_index + gap + 1
                    skip = False
                else:
                    skip = True

            gaps = [gaps[0] - 2, gaps[1] + 2]
            row_index += 1
        return res

