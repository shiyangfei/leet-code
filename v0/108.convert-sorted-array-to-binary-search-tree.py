#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
#
# Easy (41.54%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math


class Solution(object):
    def helper(self, data_list, left, right):
        if left > right:
            return None
        mid = int(math.floor((left + right) / 2))
        node = TreeNode(data_list[mid])
        node.left = self.helper(data_list, left, mid - 1)
        node.right = self.helper(data_list, mid + 1, right)
        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        return self.helper(nums, 0, length - 1)
