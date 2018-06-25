#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree
#
# Easy (37.00%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# 
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def calculate_depth(self, node, current_depth, node_depth):
        if current_depth > node_depth:
            node_depth = current_depth
        if node.left:
            left_depth = current_depth + 1
            node_depth = self.calculate_depth(node.left, left_depth, node_depth)
        if node.right:
            right_depth = current_depth + 1
            node_depth = self.calculate_depth(node.right, right_depth, node_depth)
        return node_depth

    def get_node_depth(self, node):
        if node is None:
            return 0
        depth = self.calculate_depth(node, 1, 1)
        return depth

    def is_node_balanced(self, node):
        if node is None:
            return True
        is_left_balanced = self.is_node_balanced(node.left)
        if is_left_balanced is False:
            return False
        is_right_balanced = self.is_node_balanced(node.right)
        if is_right_balanced is False:
            return False
        self_balanced = abs(self.get_node_depth(node.left) - self.get_node_depth(node.right)) <= 1
        if self_balanced is False:
            return False
        return True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_node_balanced(root)
