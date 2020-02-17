#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (46.76%)
# Total Accepted:    250.3K
# Total Submissions: 533.9K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        if rowIndex == 0:
            return row
        i = 1
        while i <= rowIndex:
            row = self.get_new_row(row)
            i += 1
        return row

    def get_new_row(self, last_row):
        new_row = []
        last_num = 0
        for num in last_row:
            new_row.append(num + last_num)
            last_num = num
        new_row.append(last_row[len(last_row) - 1])
        return new_row
