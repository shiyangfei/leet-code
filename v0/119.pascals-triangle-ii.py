#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii
#
# Easy (36.15%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Given an index k, return the kth row of the Pascal's triangle.
# 
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# 
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, rowIndex + 1):
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
        return result[rowIndex]
