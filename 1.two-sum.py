#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (45.05%)
# Total Accepted:    2.5M
# Total Submissions: 5.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        assert len(nums) >= 2
        assert target is not None
        holder = dict()
        for i, num in enumerate(nums):
            if holder.get(num) is not None:
                return [holder.get(num), i]
            holder[target - num] = i
        print('cannot find numbers that sums to target')
        return None
