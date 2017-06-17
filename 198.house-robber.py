#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber
#
# Easy (38.49%)
# Total Accepted:    134134
# Total Submissions: 348509
# Testcase Example:  '[]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases. Also thanks to @ts for adding additional test cases.
#
import math

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        result_even = 0
        result_odd = nums[0]
        # TODO: need to revisit this
