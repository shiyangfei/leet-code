#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays
#
# Easy (47.02%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n[]'
#
# 
# Given two arrays, write a function to compute their intersection.
# 
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
# 
# 
# Note:
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
# 
#
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        num_map = dict()
        for index1, num1 in enumerate(nums1):
            if num1 not in num_map:
                num_map[num1] = False
        for index2, num2 in enumerate(nums2):
            if num2 in num_map:
                num_map[num2] = True
        for key in num_map:
            if num_map[key]:
                result.append(key)
        return result
