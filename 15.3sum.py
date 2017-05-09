#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum
#
# Medium (21.48%)
# Total Accepted:    205350
# Total Submissions: 955846
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array S of n integers, are there elements a, b, c in S such that a +
# b + c = 0? Find all unique triplets in the array which gives the sum of
# zero.
# 
# Note: The solution set must not contain duplicate triplets.
# 
# 
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        level_1_num_map = {}
        for level_1_index, level_1_num in enumerate(nums):
            if level_1_num in level_1_num_map:
                continue
            level_1_num_map[level_1_num] = True
            level_1_target = 0 - level_1_num
            level_2_num_map = {}
            for level_2_index, level_2_num in enumerate(nums):
                if level_2_index == level_1_index:
                    continue
                if level_2_num in level_2_num_map:
                    continue
                level_2_num_map[level_2_num] = level_1_target - level_2_num





