#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree
#
# Easy (51.93%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_depth(self, node, depth, max_depth):
        if depth > max_depth:
            max_depth = depth
        if node.left:
            left_depth = depth + 1
            max_depth = self.get_depth(node.left, left_depth, max_depth)
        if node.right:
            right_depth = depth + 1
            max_depth = self.get_depth(node.right, right_depth, max_depth)
        return max_depth

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        max_depth = self.get_depth(root, 1, 1)
        return max_depth
