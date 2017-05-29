#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree
#
# Easy (32.82%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def get_depth(self, node, depth, min_depth):
        if node.left is None and node.right is None:
            if depth < min_depth:
                min_depth = depth
                return min_depth
        if node.left:
            left_depth = depth + 1
            min_depth = self.get_depth(node.left, left_depth, min_depth)
        if node.right:
            right_depth = depth + 1
            min_depth = self.get_depth(node.right, right_depth, min_depth)
        return min_depth

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return int(self.get_depth(root, 1, float("inf")))
