#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle
#
# Easy (37.88%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# 
# For example, given numRows = 5,
# Return
# 
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
        result = []
        for i in range(0, numRows):
            if i == 0:
                row = [1]
            else:
                row = []
                for j in range(0, i + 1):
                    last_row = result[i - 1]
                    num_1 = last_row[j - 1] if j > 0 else 0
                    num_2 = last_row[j] if j < len(last_row) else 0
                    row.append(num_1 + num_2)
            result.append(row)
        return result
