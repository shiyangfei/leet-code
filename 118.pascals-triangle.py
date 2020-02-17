#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (49.85%)
# Total Accepted:    331.6K
# Total Submissions: 663.4K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        i = 2
        while i <= numRows:
            self.add_one_row(res)
            i += 1
        return res

    def add_one_row(self, res):
        last_row = res[len(res) - 1]
        new_row = []
        last_num = 0
        for num in last_row:
            new_row.append(num + last_num)
            last_num = num
        new_row.append(last_row[len(last_row) - 1])
        res.append(new_row)
