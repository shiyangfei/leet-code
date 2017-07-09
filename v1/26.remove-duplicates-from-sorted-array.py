#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array
#
# Easy (35.54%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# 
# Given a sorted array, remove the duplicates in place such that each element
# appear only once and return the new length.
# 
# 
# Do not allocate extra space for another array, you must do this in place with
# constant memory.
# 
# 
# 
# For example,
# Given input array nums = [1,1,2],
# 
# 
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively. It doesn't matter what you leave beyond the new
# length.
# 
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        result = 0
        for index, num in enumerate(nums):
            if index == 0:
                nums[result] = num
                result += 1
                continue
            if num != nums[index - 1]:
                nums[result] = num
                result += 1
        return result
