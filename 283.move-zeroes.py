#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes
#
# Easy (49.47%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0,1,0,3,12]'
#
# 
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# 
# 
# For example, given nums  = [0, 1, 0, 3, 12], after calling your function,
# nums should be [1, 3, 12, 0, 0].
# 
# 
# 
# Note:
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_indexes = []
        index = 0
        length = len(nums)
        while index < length:
            if nums[index] == 0:
                zero_indexes.append(index)
            else:
                if len(zero_indexes) > 0:
                    first_zero_index = zero_indexes[0]
                    nums[first_zero_index] = nums[index]
                    for index1, zero_index in enumerate(zero_indexes):
                        zero_indexes[index1] = zero_index + 1
                        nums[zero_indexes[index1]] = 0
            index += 1
