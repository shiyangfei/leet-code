#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number
#
# Easy (27.76%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
# 
# Example 1:
# 
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
# 
# 
# 
# Example 2:
# 
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
# 
# 
# 
# Example 3:
# 
# Input: [2, 2, 3, 1]
# 
# Output: 1
# 
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 
# 
#
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_list = [None, None, None]
        for index, num in enumerate(nums):
            for index_max, max_num in enumerate(max_list):
                if max_num == num:
                    # prevent inserting duplicated num into max_list
                    break
                if max_num is None or num > max_num:
                    max_list.insert(index_max, num)
                    max_list = max_list[0:3]
                    break
        return max_list[2] if max_list[2] is not None else max_list[0]
