#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (62.73%)
# Total Accepted:    632.6K
# Total Submissions: 1M
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#
class Solution(object):
    # will one number appear more than 2 times?

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once_set = set()
        twice_set = set()
        for num in nums:
            if num in once_set:
                once_set.remove(num)
                twice_set.add(num)
            else:
                once_set.add(num)
        return once_set.pop()
