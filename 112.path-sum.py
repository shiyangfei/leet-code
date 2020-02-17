#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (39.74%)
# Total Accepted:    405.5K
# Total Submissions: 1M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # what if root is None
    def helper(self, node, curr_sum, target):
        new_sum = curr_sum + node.val
        if node.left is None and node.right is None:
            return new_sum == target
        res_right = self.helper(node.right, new_sum, target) if node.right is not None else False
        res_left = self.helper(node.left, new_sum, target) if node.left is not None else False
        return res_left or res_right

    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: bool
        """
        curr_sum = 0
        return target is None if root is None else self.helper(root, curr_sum, target)
