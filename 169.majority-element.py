# coding=utf-8
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element
#
# Easy (45.99%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        num_map = dict()
        for index, num in enumerate(nums):
            if num_map.get(num, None) is not None:
                num_map[num] = num_map.get(num) + 1
            else:
                num_map[num] = 1
            if num_map.get(num) > length / 2:
                return num
