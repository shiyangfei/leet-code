#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (42.46%)
# Total Accepted:    397.7K
# Total Submissions: 935.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
# 
# 
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # is root possible to be None?

    def helper(self, n, curr_dep):
        if n.left is None and n.right is None:
            return True, curr_dep
        else:
            is_left_bal = True
            is_right_bal = True
            left_dep = curr_dep
            right_dep = curr_dep
            if n.right is not None:
                is_right_bal, right_dep = self.helper(n.right, curr_dep + 1)
            if n.left is not None:
                is_left_bal, left_dep = self.helper(n.left, curr_dep + 1)
            return is_right_bal and is_left_bal and (-1 <= left_dep - right_dep <= 1), max(left_dep, right_dep)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        is_bal, dep = self.helper(root, 1)
        return is_bal
