#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum
#
# Easy (32.69%)
# Total Accepted:    489291
# Total Submissions: 1496835
# Testcase Example:  '[3,2,4]\n6'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for index, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], index]
            num_map[num] = index

# Solution().twoSum([3, 2, 4], 6)
