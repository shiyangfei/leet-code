#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii
#
# Easy (44.48%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n[]'
#
# 
# Given two arrays, write a function to compute their intersection.
# 
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
# 
# 
# Note:
# 
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# 
# 
# 
# Follow up:
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = []
        num_map1 = dict()
        num_map2 = dict()
        for index1, num1 in enumerate(nums1):
            if num1 not in num_map1:
                num_map1[num1] = 0
            num_map1[num1] += 1
        for index2, num2 in enumerate(nums2):
            if num2 not in num_map2:
                num_map2[num2] = 0
            num_map2[num2] += 1
        for key in num_map1:
            if key in num_map2:
                count = min(num_map1[key], num_map2[key])
                unit_result = [key] * count
                result += unit_result
        return result
