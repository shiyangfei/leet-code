#
# @lc app=leetcode id=107 lang=python
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (49.76%)
# Total Accepted:    276.4K
# Total Submissions: 554.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def __init__(self):
        self.res = []

    def process_node(self, n, level):
        if n is None:
            return
        expected_level_res_index = len(self.res) - level
        # if level res is not there, init it
        if expected_level_res_index == -1:
            self.res.insert(0, [])
            expected_level_res_index = 0
        level_res = self.res[expected_level_res_index]
        level_res.append(n.val)
        self.process_node(n.left, level + 1)
        self.process_node(n.right, level + 1)

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.process_node(root, 1)
        return self.res
