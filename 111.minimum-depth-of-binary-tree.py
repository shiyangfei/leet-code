#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (36.51%)
# Total Accepted:    364.9K
# Total Submissions: 998.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
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

    def __init__(self):
        self.res = None

    def helper(self, n, curr_dep):
        if n.left is None and n.right is None:
            self.res = curr_dep if self.res is None else min(self.res, curr_dep)
        if n.left is not None:
            self.helper(n.left, curr_dep + 1)
        if n.right is not None:
            self.helper(n.right, curr_dep + 1)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root, 1)
        return self.res
