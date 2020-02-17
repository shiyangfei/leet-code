#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (54.82%)
# Total Accepted:    345.3K
# Total Submissions: 628K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def process_array(self, arr):
        if len(arr) == 0:
            return None
        if len(arr) == 1:
            return TreeNode(arr[0])
        mid_index = int((len(arr) / 2))
        head = TreeNode(arr[mid_index])
        if mid_index > 0:
            left_arr = arr[:mid_index]
            head.left = self.process_array(left_arr)
        if mid_index < len(arr) - 1:
            right_arr = arr[mid_index+1:]
            head.right = self.process_array(right_arr)
        return head


    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.process_array(nums)
