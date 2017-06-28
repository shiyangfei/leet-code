#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate
#
# Easy (45.30%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# 
# Given an array of integers, find if the array contains any duplicates. Your
# function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
# 
#
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_map = dict()
        for index, num in enumerate(nums):
            if num in num_map:
                return True
            num_map[num] = True
        return False
