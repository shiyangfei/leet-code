#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii
#
# Easy (39.23%)
# Total Accepted:    
# Total Submissions: 
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
        self.result = []

    def add_node(self, node, depth):
        if len(self.result) <= depth:
            self.result.append([])
        self.result[depth].append(node.val)
        if node.left:
            self.add_node(node.left, depth + 1)
        if node.right:
            self.add_node(node.right, depth + 1)

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is not None:
            self.add_node(root, 0)
        self.result.reverse()
        return self.result
