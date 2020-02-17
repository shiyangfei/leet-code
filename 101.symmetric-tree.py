#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (45.50%)
# Total Accepted:    546.8K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
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
    def are_nodes_sym(self, n_l, n_r):
        if n_l is None and n_r is None:
            return True
        if n_l is not None and n_r is None:
            return False
        if n_l is None and n_r is not None:
            return False
        if n_l.val != n_r.val:
            return False
        return self.are_nodes_sym(n_l.left, n_r.right) and self.are_nodes_sym(n_l.right, n_r.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.are_nodes_sym(root.left, root.right)
