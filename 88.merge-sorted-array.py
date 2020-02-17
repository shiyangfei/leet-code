#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (37.96%)
# Total Accepted:    488.5K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
#
class Solution(object):
    # positive integers?
    def insert(self, nums1, num, index):
        nums1.insert(index, num)
        nums1.pop()

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        while i2 < n and i1 < m + n:
            num1 = nums1[i1]
            num2 = nums2[i2]
            if num2 <= num1 or i1 >= m + i2:
                self.insert(nums1, num2, i1)
                i2 += 1
            i1 += 1
