#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii
#
# Easy (32.14%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n0'
#
# 
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
#
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_map = dict()
        for index, num in enumerate(nums):
            if num in num_map and index - num_map[num] <= k:
                    return True
            num_map[num] = index
        return False
